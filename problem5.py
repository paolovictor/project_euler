n = 20
n1to20 = range(1,21)
while n <= 2432902008176640000:
    if n % 100000000 == 0:
        print "[", n, "]"
    for i in n1to20:
        if n % i != 0:
            break
        elif i == 20:
            print "RESULT", n, i
            n = 2432902008176640000
            break
    n += 20
