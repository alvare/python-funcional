#!/usr/bin/python3
# -*- coding: utf-8 -*-
from functools import reduce
from pymonad.Monad import Monad

class Parser(Monad):
    @classmethod
    def unit(cls, value):
        return Parser(lambda cs: [(value, cs)])

    def bind(self, f):
        return Parser(lambda cs: concat([(f(a)).value(cs2) for (a, cs2) in self.value(cs)]))

def parse(parser, string):
    val = parser.value(string)
    if val:
        return val[0][0]
    else:
        return "error"

def concat(ls):
    return reduce(lambda x, y: x+y, ls, [])
