#ВАРИАНТ 4 (ЗАДАНИЕ 3)
def gen(x):

    if x % 2 == 0:
        for i in range(x):
            yield '@'*x
    else:
        for i in range(x):
            yield ' '*abs(x//2-i) + '1'*(x-abs(x//2-i)*2) + ' '* abs(x//2-i)

for i in gen(4):
    print(i)
for i in gen(5):
    print(i)

#0_-