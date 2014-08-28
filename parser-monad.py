import sys
from pymonad.Reader import curry
from Parser import Parser, parse

def item():
    return Parser(lambda cs: [] if cs == "" else [(cs[0], cs[1:])])

def one_and_third():
    return item() >> (lambda a:
           item() >>
           item() >> (lambda b:
           Parser.unit(a + b)))

def fifth():
    return one_and_third() >> (lambda a:
           item() >>
           item() >> (lambda y:
           Parser.unit(a + y)))


print(parse(fifth(), sys.argv[1]))
