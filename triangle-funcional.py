from functools import partial


triangles = [sum(range(x + 1)) for x in range(250)]
divides = lambda a, d: a % d == 0
divisors = lambda x: filter(partial(divides, x), range(1, x + 1))
divCount = lambda x: len(divisors(x))

tridivsnum = zip(triangles, map(divCount, triangles), range(250))
print filter(lambda t: t[1] > 50, tridivsnum)[0]
