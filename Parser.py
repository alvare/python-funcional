#!/usr/bin/python3
# -*- coding: utf-8 -*-
from functools import reduce
from pymonad.Monad import *
from pymonad.Monoid import *

class Parser(Monoid, Monad):
    @classmethod
    def unit(cls, value):
        return Parser(lambda cs: [(value, cs)])

    def bind(self, f):
        return Parser(lambda cs: concat([(f(a)).value(cs2) for (a, cs2) in self.value(cs)]))

    @staticmethod
    def mzero():
        return Parser(lambda cs: [])

    def mplus(self, b):
        return Parser(lambda cs: self.value(cs) + b.value(cs))

    def __or__(self, b):
        return Parser(lambda cs: (lambda y: [] if not y else [y[0]])((self + b).value(cs)))

    def parse(self, string):
        val = self.value(string)
        if val:
            return val
        else:
            return "error"

def concat(ls):
    return reduce(lambda x, y: x+y, ls, [])
