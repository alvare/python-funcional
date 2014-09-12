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
           unit(Parser, reduce(lambda x, y: x + y, w, '')))

def array_parser():
    return string('array') >>\
           space() >>\
           char('[') >>\
           sepby(word(), char(',')) >> (lambda e:
           char(']') >>
           unit(Parser, e))

print(array_parser().parse(sys.argv[1]))
