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

print tri, divcount, n
