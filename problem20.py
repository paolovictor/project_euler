def fatorial(n):
    if n <= 1:
        return 1

    x = n
    while x % 10 == 0:
        x /= 10

    return x * fatorial(n-1)

print sum([int(c) for c in str(fatorial(100))])
