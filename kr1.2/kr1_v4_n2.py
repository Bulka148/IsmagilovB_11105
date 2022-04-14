#ВАРИАНТ 4 (ЗАДАНИЕ 2)

class MyIterator:
    def __init__(self, st):
        self.st = st
        self.st1 = ''
        self.index = 0
        self.k = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.k == 0:
            self.k = 1
            return ' '
        else:
            if self.st1 != self.st:
                self.st1 = self.st1 + self.st[self.index]
                self.index = self.index + 1
                return self.st1
            else:
                raise StopIteration

a = MyIterator('Hello there!')
for i in a:
    print(i)

#-_0