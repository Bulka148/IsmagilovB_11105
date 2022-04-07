#2 ВАРИАНТ (3 ЗАДАНИЕ)

def gen(stroka):
    while True:
        for charlie in stroka:
            yield charlie

        for charlie in reversed(stroka):
            yield charlie


