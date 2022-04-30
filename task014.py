
import re

s = 'aaab aaaac aaad ae ad b aed'

print(re.findall(r'\ba+[^b]\b', s))