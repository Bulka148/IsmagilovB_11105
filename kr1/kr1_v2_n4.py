#2 ВАРИАНТ (4 ЗАДАНИЕ)
import re

st = '011011111 1010000111 1010100110 011101 10 1 0 11110 10100 1100011 1010101001010101'
print(re.findall(r'011\d*', st))
print(re.findall(r'\d*010\d*', st))
print(re.findall(r'\d*00\d*11|\d*11\d*00\d*', st))
