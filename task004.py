from functools import reduce

a = input().split(',')
a_pr = list(filter(lambda s: len(set(s.lower())) > 3, a))
a1 = list(map(lambda s: (s[0].upper() if 'a' <= s[0] <= 'z' else s[0].lower()) + s[1:], a_pr))
summ = reduce(lambda l1, l2: l1 + l2, [len(s) for s in a if s.count('foo') > 0])

print(a1, summ)