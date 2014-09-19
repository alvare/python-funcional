from random import randint
from fn import _

def quicksort(l):
    if len(l) > 0:
        h = l[0]
        t = l[1:]
        smaller = filter(_ < h, t)
        bigger = filter(_ >= h, t)
        return quicksort(smaller) + [h] + quicksort(bigger)
    else:
        return []

unsorted = map(lambda _: randint(0, 100), range(100))
print quicksort(unsorted)
