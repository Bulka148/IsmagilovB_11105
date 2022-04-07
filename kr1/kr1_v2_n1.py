#2 ВАРИАНТ (1 ЗАДАНИЕ)

from functools import reduce

fact = lambda n: [reduce(lambda a, b: a*b, range(1, i+1)) for i in range(1, n+1)]
fact_sqr = lambda n: [reduce(lambda a,b: a*b, range(1, i+1))**0.5 for i in range(1, n+1)]

print(fact(7))