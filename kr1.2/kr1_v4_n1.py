#ВАРИАНТ 4 (ЗАДАНИЕ 1)

a = lambda x: [1 if i == 0 else 2**i for i in range(x)]
foo = lambda x: filter(lambda i: '2' in str(i), a(x))
foo1 = lambda x, y: map(lambda x: x**y, foo(x))
print(list(foo(10)))
print(list(foo1(10, 2)))