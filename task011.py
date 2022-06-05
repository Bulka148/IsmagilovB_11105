# глобальная переменная
v1: str = 'Python'


class Class:
    global v1

    def metod1(self, sep1: str = ' ', sep2: str = ' ', end: str='!') -> str:
        def metod2() -> str:
            # локальная переменная
            v3: str = 'best'
            return v3

        # полулокальная(enclosing) переменная
        v2: str = 'is the'

        return v1 + sep1 + v2 + sep2 + metod2() + end


myclass = Class()
print(myclass.metod1())