n1to100 = range(1,101)
print abs(sum(map(lambda x : x ** 2, n1to100)) - (sum(n1to100) ** 2))
