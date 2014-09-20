from operator import *

add(5, 6) => 11
methodcaller('split', ',')('1,2,3') => [1, 2, 3]

from itertools import *

chain(['a', 'b', 'c'], xrange(4)) => ['a', 'b', 'c', 0, 1, 2, 3]
takewhile(lambda x: x < 5, count(2)) => [2, 3, 4]
repeat(10, 3) => [10, 10, 10]

from functools import reduce

reduce(lambda x, y: x - y, [1,2,3,4], 0) => -10
