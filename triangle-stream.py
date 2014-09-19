from fn import Stream, F
from fn.iters import *
from operator import add, lt, itemgetter
from itertools import count


s = Stream()
triangles = s << [1] <<  map(add, count(2), s)

divides = lambda a, d: a % d == 0
divisors = lambda x: filter(partial(divides, x), range(1, x + 1))
divCount = lambda x: len(list(divisors(x)))

second = itemgetter(1)
tridivsnum = zip(triangles, map(divCount, triangles), count(1))

print head(filter(F(lt, 50) << second, tridivsnum))
