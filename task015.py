import re

s = 'b a ab aaabbb aaacccbbbb aaaccccbbbb aaacccccbb aaaabb aaaaabb'

print(re.findall(r'\ba(?:aa)*(?:|ccc|ccccc)(?:bb)+\b', s))