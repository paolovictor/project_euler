fib1, fib2 = 1, 1
i, soma = 0, 0

while i < 4000000:
    i = fib1 + fib2
    if i % 2 == 0:
        soma += i
    fib1, fib2 = fib2, i
    
print soma
