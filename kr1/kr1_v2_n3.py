#2 ВАРИАНТ (3 ЗАДАНИЕ)

def gen(st):
    while True:
        for charlie in st:
            yield charlie

        for charlie in reversed(st):
            yield charlie


