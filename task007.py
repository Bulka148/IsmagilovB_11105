class My_strange_class:

    def __init__(self, start=0):
        self.num = start
        self.pow = -1

    def ch_figures(self):
        for c in str(self.num):
            if int(c) % 2 == 0:
                yield int(c)

    def simp_numbers(self):
        for i in range(2, self.num+1):
            if len([d for d in range(2, int(i**0.5)+1) if i % d == 0]) == 0:
                yield i

    def fig_simp_numbs(self):
        simp_numb = list(self.simp_numbers())
        simp_fig = set(map(int, list(str(self.num))))
        print(simp_fig)
        for i in range(self.num + 1):
            simp_mn = set(d for d in range(2, i + 1) if i % d == 0 and d in simp_numb)
            if simp_mn | simp_fig == simp_fig:
                yield i

    def __iter__(self):
        return self

    def __next__(self):
        self.pow += 1
        return self.num ** self.pow


a = My_strange_class(123)
print(list(a.fig_simp_numbs()))