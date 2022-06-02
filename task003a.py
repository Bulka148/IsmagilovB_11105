st = input().split()
i = 0
while i < len(st):
    if (st[i] == '+' or
        st[i] == '-' or
        st[i] == '*' or
        st[i] == '/'):

        st[i-2] = '('+st[i-2]+st[i]+st[i-1]+')'
        st.pop(i) and st.pop(i-1)
        i = i - 1

    else:
        i = i + 1
print(st.pop())
