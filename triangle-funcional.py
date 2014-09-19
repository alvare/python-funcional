from functools import partial
from itertools import count


triangles = [sum(range(x + 1)) for x in range(250)]
divides = lambda a, d: a % d == 0
divisors = lambda x: filter(partial(divides, x), range(1, x + 1))
divCount = lambda x: len(divisors(x))

print filter(lambda t: t[1] > 50, zip(triangles, map(divCount, triangles), range(240)))[0]
