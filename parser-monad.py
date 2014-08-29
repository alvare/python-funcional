import sys
from pymonad.Reader import curry
from Parser import *

def item():
    return Parser(lambda cs: [] if cs == "" else [(cs[0], cs[1:])])

def sat(cond):
    return item() >> (lambda c: unit(Parser, c) if cond(c) else mzero(Parser))

def char(c):
    return sat(lambda x: c == x)

def space():
    return char(' ')

def oneOf(chars):
    return sat(lambda x: x in chars)

def many(p):
    return many1(p) | unit(Parser, [])

def many1(p):
    return p >> (lambda x:
           many(p) >> (lambda xs:
           unit(Parser, [x] + xs)))

def sepby(p, sep):
    return sepby1(p, sep) | unit(Parser, [])

def sepby1(p, sep):
    return p >> (lambda x:
           many(sep >> p) >> (lambda xs:
           unit(Parser, [x] + xs)))

def string(s):
    if s:
        return char(s[0]) >>\
               string(s[1:]) >>\
               unit(Parser, s)
    else:
        return unit(Parser, '')

def chainl(p, op, a):
    return chainl1(p, op) | unit(Parser, a)

def chainl1(p, op):
    def rest(a):
        return (op >> (lambda f: p >> (lambda b: rest(f(a, b))))) | unit(Parser, a)
    return p >> rest

# examples
alpha = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'

def word():
    return many(oneOf(alpha)) >> (lambda w:
           unit(Parser, mconcat(w)))

def array_parser():
    return string('array') >>\
           space() >>\
           char('[') >>\
           sepby(word(), char(',')) >> (lambda e:
           char(']') >>
           unit(Parser, e))

def n_array_to_int(ls):
    return reduce(lambda x, y: x + y, map(lambda k: int(k[0]) * pow(10, k[1]), zip(ls, reversed(range(len(ls))))), 0)

def dispatch(op):
    if op == '+':
        return lambda x, y: x + y
    elif op == '-':
        return lambda x, y: x - y

def number():
    return many(oneOf(num)) >> (lambda ns:
           many(space()) >> (lambda _:
           unit(Parser, n_array_to_int(ns))))

def oper():
    return oneOf('+-') >> (lambda op:
           many(space()) >>
           unit(Parser, dispatch(op)))

def math_parser():
    return chainl1(number(), oper())

print(math_parser().parse(sys.argv[1]))
