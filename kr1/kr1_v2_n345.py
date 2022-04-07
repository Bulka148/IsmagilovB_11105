#2 ВАРИАНТ (3 ЗАДАНИЕ И 4 ЗАДАНИЕ И 5 ЗАДАНИЕ)
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

#5
pats = [r'\b1(0|11)\b', r'\b[01]?10?1?\b', r'\b11(00|11|11)?\b']
with open('task5_output', 'w') as f:
    for p in pats:
        f.write(str(re.findall(p, stroka)) + '\n')