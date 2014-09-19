from fn import _, Stream, F
from fn.iters import range, filter, map, zip, head
from operator import add, lt, itemgetter
from itertools import count


s = Stream()
triangles = s << [1] <<  map(add, count(2), s)

divides = lambda a, d: a % d == 0
divisors = lambda x: filter(F(divides, x), range(1, x + 1))
divCount = lambda x: len(list(divisors(x)))
second = itemgetter(1)
print head(filter(F(lt, 50) << second, zip(triangles, map(divCount, triangles), count(1))))
