import math

sqrt2 = math.sqrt(2)

total_area = 250 * 250
ratio = lambda a,x,y : float(a) / float(x + y)

cut = 0.0
max_ratio = 0.0

max_ratio = 0
m = range(0, 251)
n = range(0, 251)
for (cut_a, cut_b) in ((i,k) for i in m for k in n):
    cut_a, cut_b = float(cut_a), float(cut_b)

    area = total_area - ((cut_a * cut_b) / 2.0)
    diag = math.sqrt(cut_a**2 + cut_b**2)
    r = ratio(area,  500 - cut_a - cut_b, diag)
    max_ratio = r > max_ratio and r or max_ratio

    if cut_a == 75.0 and cut_b == 75.0:
        print cut_a, cut_b, r

print "%.8f" % max_ratio
