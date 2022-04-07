#2 ВАРИАНТ (3 ЗАДАНИЕ И 4 ЗАДАНИЕ)
import re

#3
def gen(stroka):
    while True:
        for charlie in stroka:
            yield charlie

        for charlie in reversed(stroka):
            yield charlie

#4
stroka = '011011111 1010000111 1010100110 011101 10 1 0 11110 10100 1100011 1010101001010101'
print(re.findall(r'011\d*', stroka))
print(re.findall(r'\d*010\d*', stroka))
print(re.findall(r'\d*00\d*11|\d*11\d*00\d*', stroka))
