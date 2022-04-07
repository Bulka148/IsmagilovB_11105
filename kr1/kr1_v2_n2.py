#2 ВАРИАНТ (2 ЗАДАНИЕ)

class MyIterator:
    def __init__(self, stroka, n):
        self.n, self.ind = n, -1
        self.glas = [c for c in stroka if c in ['a', 'i', 'o', 'u', 'y', 'e']]

    def __iter__(self):
        for c in self.glas:
            yield c

    def __next__(self):
        self.ind += 1
        if self.ind == self.n:
            raise Exception('error')
        return self.glas[self.ind % len(self.glas)]

