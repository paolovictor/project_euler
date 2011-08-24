import math

for a in xrange(1, 1001):
    for b in xrange(a + 1, 1001):
        c = int(math.sqrt(a**2 + b**2))
        if a + b + c == 1000 and a**2 + b**2 == c**2:
            print a*b*c
