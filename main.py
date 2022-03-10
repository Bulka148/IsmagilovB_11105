#1
# a = [25, 23, 45, 21, 25]
# #a = [44, 23, 65, 43]
# f = False
# for i in range(len(a)):
#     ff = False
#     while a[i] > 0:
#         if a[i] % 2 == 1:
#             ff = True
#         a[i] //= 10
#     if ff == False:
#         f = True
#
# print(f)


#2
#
def factorial(a):
    for i in range(a-1, 2, -1):
        a *= 1
    return a

n, x = list(map(int, input().split()))

sum_n = 0
for k in range(1, n+1):
    sum_n += ((-1)**k)*((x**(2*k+1))/((factorial(k) + x)))

print(sum_n)


# #3
a = []
n = int(input())
for i in range(n):
    a.append(list(map(int, input().split())))


b = [0]*10
for i in range(len(a)):
    for j in range(len(a[i])):
        while a[i][j] > 0:
            b[a[i][j] % 10] += 1
            a[i][j] //= 10

for i in range(0,10):
    print(str(i) + ':',  b[i], "times")