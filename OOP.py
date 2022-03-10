class Link:
    def __init__(self, value=None):
        self.next = None
        self.prev = None
        self.value = value
class Deque:
    def __init__(self):
        self.head = Link()
        self.head.prev = self.head
    def pushleft(self, value):
        new = Link(value)
        new.next = self.head.next
        new.prev = self.head
        self.head.next.prev = new
        self.head.next = new
    def pushright(self, value):
        last = Link(value)
        self.head.prev.next = last
        last.prev = self.head.prev
        self.head.prev = last
    def popleft(self):
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
    def popright(self):
        self.head.prev = self.head.prev.prev
        self.head.prev.next = None
    def __str__(self):
        s = ''
        now = self.head.next
        while now is not None:
            s += str(now.value) + ' '
            now = now.next
        return s

a = Deque()
a.pushright(1)
a.pushleft(2)
a.pushleft(3)
a.popright()
a.pushleft(5)
print(a)














































# class LinkedList:
#     def __init__(self, value):
#         self.next = None
#         self.prev = None
#         self.value = value
#
#
# class Deque:
#     def __init__(self, value=None):
#         self.head = LinkedList(value)
#
#     def pushleft(self, value):
#         first = self.head
#         last = self.head.prev
#         self.head = LinkedList(value)
#         self.head.prev = last
#         self.head.next = first
#
#     def pushright(self, value):
#         last = LinkedList(value)
#         last.prev = self.head.prev
#         self.head.prev.next = last
#         self.head.prev = last
#
#     def popleft(self):
#         last = self.head.prev
#         self.head = self.head.next
#         self.head.prev = last
#
#     def popright(self):
#
#
# head = Deque()
# head.pushright(1)
#




# class PseudoArray:
#     next = prev = None
#
#     def __init__(self, length):
#         self.dim = length
#         self.internal = [None] * length
#
#     def __getitem__(self, index):
#         return self.internal[index]
#
#     def __setitem__(self, index, value):
#         self.internal[index] = value
#
#     def __len__(self):
#         return self.dim
#
#
# class LinkedArray:
#     next = prev = None
#
#     def __init__(self):
#         self.base = PseudoArray(1)
#         self.base.prev = self.base
#         self.length = 0
#
#     def _now_ind(self):
#         k, leng = 1, self.length
#         while leng - k > 0:
#             leng -= k
#             k *= 2
#         return leng - 1
#
#     def append(self, value):
#         self.length += 1
#         now = self.base.prev
#
#         if self._now_ind() == 0 and self.length != 1:
#             last = PseudoArray(self.length)
#             last.internal[0] = value
#             now.next = last
#             last.prev = now
#             self.base.prev = last
#         else:
#             now.internal[self._now_ind()] = value
#
#     def delete(self):
#         if self.length == 0:
#             return 0
#
#         now = self.base.prev
#         now.internal[self._now_ind()] = None
#         if self._now_ind() == 0:
#             now.prev.next = None
#             self.base.prev = now.prev
#         self.length -= 1
#
#     def get(self, index) -> object:
#         now = self.base.prev
#         k = self.length - self._now_ind() - 1
#         while k > index:
#             now = now.prev
#             k -= len(now)
#
#         return now.internal[index - len(now) + 1]
#
#     def represent(self) -> str:
#         now = self.base
#         val = [str(self.base.internal[0])]
#         while now.next is not None:
#             val.append(' ')
#             now = now.next
#             n = len(now) if now.next is not None else self._now_ind() + 1
#             for ind in range(n):
#                 val.append(str(now[ind]))
#
#         return ' '.join(val)
#
#     def __getitem__(self, index):
#         return self.get(index)
#
#     def __repr__(self):
#         return self.represent()
#
#     def __len__(self):
#         return self.length
#
#
# arr = LinkedArray()
# for i in range(1, 20):
#     arr.append(i)
#     print(arr)
#
# print('elements: ', end='')
# for i in range(len(arr) - 1):
#     print(arr[i], end=', ')
# print(arr[len(arr) - 1])
#
# for i in range(18):
#     arr.delete()
#     print(arr)





































































# a = input()
# print(ord(a))
# a = int(input())
# if a == 0:
#     print(a, "программистов")
# # if a == 1:
# #     print(a, "программист")
# # if 2<=a<=4:
# #     print(a, "программиста")
# # if 5<=a<=20:
# #     print(a, "программистов")
# if a % 10 == 1 or  a % 100 == 1:
#     print(a, "программист")
# if a % 10 == 2 or  a % 100 == 2:
#     print(a, "программиста")
# if a % 10 == 3 or  a % 100 == 3:
#     print(a, "программиста")
# if a % 10 == 4 or  a % 100 == 4:
#     print(a, "программиста")
# if a % 10 == 5 or  a % 100 == 5:
#     print(a, "программистов")
# if a % 10 == 6 or  a % 100 == 6:
#     print(a, "программистов")
# if a % 10 == 7 or  a % 100 == 7:
#     print(a, "программистов")
# if a % 10 == 8 or  a % 100 == 8:
#     print(a, "программистов")
# if a % 10 == 9 or a % 100 == 9:
#     print(a, "программистов")
# if a % 100 == 11 or a % 100 == 12 or a % 100 == 13 or a % 100 == 14:
#     print(a, "программистов")



# figure = input()
# pi = 3.14
# if figure == "треугольник":
#     a = float(input())
#     b = float(input())
#     c = float(input())
#     p = ((a + b + c) / 2)
#     print((p*(p-a)*(p-b)*(p-c))**0.5)
# if figure == "круг":
#     a = float(input())
#     print(pi*(a**2))
# if figure == "прямоугольник":
#     a = float(input())
#     b = float(input())
#     print(a*b)
# a = [2,6,8,4,2,3]
# a.sort()
# print(a)
# A = int(1input())
# B = int(input())
# H = int(input())
#
# if A<=H<=B:
#     print("Это нормально")
# elif H<=A<=B:
#     print("Недосып")
# else:
#     print("Пересып")
# #2
#
# print(2**2**10%100)
# a = [2, 5, 1, 8, 9, 0]
# for i in range(len(a)-1):
#     for j in range(i+1, len(a)):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
# print(a)

# #1
# a = [2, 5, 1, 8, 9, 0]
#
#
# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
#
# print(a)








# class Abiturient:
#     def __init__(self, school, score, ):
#         self.school = school
#         self.score = score
#
# class Facultet(Abiturient):
#     def __init__(self, name, score):

















# a = [-100, -50, -20, -2]
#
# min1 = min(a)
# a.pop(a.index(min1))
# min2 = min(a)
#
# max1 = max(a)
# a.pop(a.index(max1))
# max2 = max(a)
#
# print(min(min1*min2, min1*max1, max1*max2))
#
# def gn(another_gn):
#     for i in another_gn:
#         if i % 2 == 0:
#             yield i
# print(list(gn([i for i in range(1,100)])))

# X = int(input())
# H = int(input())
# M = int(input())
# hours1 = X // 60
# minutes1 = X % 60
#
# hours2 = H + hours1
# minutes2 = M + minutes1
#
# if minutes2 > 60:
#     hours2 = hours2 + 1
#     minutes2 = minutes2 - 60
# print(hours2)
# print(minutes2)

# a = [1, 2, 4, 2, 2, 3, 2, 2, 2, 1, 5, 2, 2]
# promejutok = max(a) + 1
# b = [0]*promejutok
# for i in range(len(a)):
#     b[a[i]] += 1
#
# maxik = max(b)
#
#
# print(b.index(maxik))

# import statistics
# a = [1, 2, 4, 2, 2, 3, 2, 2, 2, 1, 5, 2, 2]
# print(statistics.mode(a))


# n = int(input())
# for i in range()
#
# n = 100
# massive = [[0]*n for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         massive[i][j] = i*j
# numpy.set_printoptions(threshold=numpy.nan)
# print(numpy.array(massive))


# x = [3, 10, 5, 25, 2, 8]
# m1 = 0
# m2 = 0
# value = 0
#
# for i in range(len(x)):
#     for j in range(len(x)):
#         if x[i] ^ x[j] > value:
#             m1 = x[i]
#             m2 = x[j]
#             value = m1 ^ m2
#
# print(value)








# x, y, z = list(map(int, input().split()))
#
# u = ((x+y+2.1)/(x-z-5.6)*z + y)*y + (z+1.1)/(z-2.0)
#
# print(u)







# def fibonachi(n):
#     a = 1
#     b = 1
#     for i in range(1,n):
#         yield a
#         c = a + b
#         a = b
#         b = c
#
# for g in fibonachi(110):
#     print(g)
#


# #Генератор
# def generator(a, n, k):
#     for i in range(a, n, k):
#         yield i
#
# a, n, k = [int(i) for i in input().split()]
#
# g = generator(a, n, k)
#
# for i in g:
#     print(i)

# def usage_of_return(number_of_value):
#     # result = [i for i in range(number_of_value)]
#     result = []
#     for i in range(number_of_value):
#         result.append(i**2)
#     return result
#
# print(usage_of_return(10))












# def some_function():
#     print(1)
#     return "Something"
#
# another_function = some_function
#
# print(another_function)
# another_function()
# def one_more_function(arg_func):
#     print("Inside one more")
#     return arg_func()
#
# print(one_more_function)
# print(one_more_function(another_function))
#
# def printing(func):
#     print(321)
#     def wrap():
#         print("Start")
#         res = func()
#         print("End")
#         return res
#     return wrap()
#
# @printing
# def example():
#     print("Middle")
#     return 123
# print(example())



















# from math import asin, degrees
# class Triange:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def c(self):
#         return (self.a * self.a + self.b * self.b) ** (0.5)
#
#     def square(self):
#         return (0.5)*(self.a * self.b)
#
#     def perimetr(self):
#         return (self.a + self.b + self.c())
#
#     def angle1(self):
#         return degrees(asin(self.a / self.c()))
#
#     def angle2(self):
#         return degrees(asin(self.b / self.c()))
#
# tria1 = Triange(6,8)
# print("c")
# print(tria1.c())
# print("Square")
# print(tria1.square())
# print("Perimetr")
# print(tria1.perimetr())
# print("Ugol1")
# print(tria1.angle1())
# print("Ugol2")
# print(tria1.angle2())

# Длина гипотнезуы 1
# Площадь 1 тругольник
# Периметр
# Угол1
# Угол2




# class Recatangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def square(self):
#         return self.a * self.b
#     def perimetr(self):
#         return 2*self.a + 2*self.b
#
# rec1 = Recatangle(5,10)
# print(rec1.square())
# print(rec1.perimetr())





















# #№1
# a = [1, 3, 3, 4, 6, 7]
# b = [4, 4, 6, 7, 8, 9, 10]
# result = []
#
# #RESULT = [1,3,3,4,4,4,6,6,7,7,8,9,10]
#
# ia = 0
# ib = 0
# for ia in range(len(a)):
#     while ib < len(b) and b[ib] <= a[ia]:
#         result.append(b[ib])
#         ib += 1
#     result.append(a[ia])
# if len(a) < len(b):
#     result = result + b[len(a)-2:]
# print(result)
#
# print('________________________')
#
# #№2
# a = [51, 26, 76, 76, 24, 45, 43]
# max_el = 0
# max_ind = 0
# for i in range(3):
#     max_el = 0
#     for j in range(len(a)):
#         if a[j] > max_el:
#             max_el = a[j]
#             max_ind = j
#     while a.count(max_el) > 0:
#         a.pop(a.index(max_el))
# print(max_el)











# a = [[1, 2, 3], [3, 2, 1]]
# b = [[4, 5, 6], [6, 5, 4]]
# c = []
# for i in range(len(a)):
#     row = [0]*len(a[i])
#     for j in range(len(a[i])):
#         row[j] = a[i][j]+b[i][j]
#     c.append(row)
# for i in range(len(c)):
#     print(c[i])
#


# a = [1, 5, 4, 2, 4, 1]
# l = len(a)
# m = 0
# cur = 0
#
# for i in range(l):
#     for j in range(i+1, l):
#         cur = (j - i) * min(a[i], a[j]) + 0.5 * ((j - i) * (max(a[i], a[j]) - min(a[i], a[j])))
#         if cur > m:
#             m = cur
# print(m)
# first = [int(i) for i in list(input())[::-1]]
# second = [int(i) for i in list(input())[::-1]]
# answer = []
# buffer = 0
# if len(second) > len(first):
#     first, second = second, first
# for i in range((max(len(first), len(second)))):
#     if len(second) - 1 >= i:
#         res = (first[i] + second[i] + buffer)
#     else:
#         res = first[i] + buffer
#     buffer = 0
#     if i < (max(len(first), len(second))) - 1:
#         answer.append(res % 10)
#     else:
#         answer.append(res)
#     if res > 10:
#         buffer += 1
#
# answer = [str(i) for i in answer]
# print(''.join(answer[::-1]))

# #2
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# def print_list(first):
#     cur = first
#     while cur is not None:
#         print(cur.value, end=" ")
#         cur = cur.next
#     print(cur)
#
# first = Node(666)
# cur = first
#
# for i in range(21):
#     node = Node(i)
#     cur.next = node
#     cur = cur.next
# print_list(first)
#
#
#
#
# def del_from_midle(first, node):
#     if first is None and first.next is None and first.next.next is None:
#         return first
#     cur = first
#     while cur.next is not None and cur.next.next is not None:
#         if cur.next.value == node.value:
#             cur.next = cur.next.next
#         else:
#             cur = cur.next
#     print_list(first)
# print_list(first)
#
#
# del_from_midle(first, Node(10))
#


# def print_list(first):
#     cur = first
#     while cur is not None:
#         print(cur.value, end=" ")
#         cur = cur.next
#     print(cur)









# def rev_list(first):
#     cur = first
#     vals = []
#     while cur is not None:
#         vals.append(cur.value)
#         cur = cur.next
#     vals.reverse()
#
#     i = 1
#     cur = first
#     while cur is not None:
#         cur.value = vals[i-1]
#         cur = cur.next
#         i += 1
#     return first
#
# first = Pepa(666)
# cur = first
#
# for i in range(21):
#     pepa = Pepa(i)
#     cur.next = pepa
#     cur = cur.next
#
# print_list(first)
# first = rev_list(first)
# print_list(first)