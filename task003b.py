s = '(' + input() + ')'

opers = ['*', '/', '+', '-']
while s.count('(') > 0:
    st_ind = s.rfind('(')
    fi_ind = st_ind + s[st_ind:].find(')')
    s1 = s[st_ind+1:fi_ind]
    for sim in opers:
        while s1.count(sim) > 0:
            oper = s1.find(sim)
            fi_2 = oper + 2
            while fi_2 < len(s1) and s1[fi_2] != ' ':
                fi_2 += 1
            s1 = s1[:oper - 1] + s1[oper + 2: fi_2] + str(opers.index(sim)) + s1[fi_2:]
    s = s[:st_ind] + s1 + s[fi_ind+1:]

for i in range(len(s)):
    if '0' <= s[i] <= '3':
        s = s[:i] + opers[int(s[i])] + s[i+1:]
print(' '.join(list(s)))