#!/usr/bin/python3
# -*- coding: utf-8 -*-
from pymonad.Reader import curry
from pymonad.List import List

@curry
def guard(cond):
    if cond:
        return List.unit(())
    else:
        return List.mzero()

val = List(1, 2) >> (lambda x:
      List(3, 4) >> (lambda y:
      guard(y == 4) >> (lambda z:
      List.unit((x, y)))))

print(val)
print([(x, y) for x in [1,2] for y in [3,4] if y == 4])
