from fn import _, Stream
from fn.uniform import *
from fn.iters import *
from itertools import count

n = 0
tri = 0
divcount = 0
while divcount < 50:
    n += 1
    tri = tri + n
    divcount = 0
    for x in range(1, tri + 1):
        if tri % x == 0:
            divcount += 1



print tri

###

s = Stream()
triangles = s << [1] <<  map(add, count(2), s)
divCount = lambda x: len(list(filter(lambda n: x % n == 0, range(1, x + 1))))
print next(filter(_[1] > 50, zip(triangles, map(divCount, triangles))))
