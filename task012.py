from functools import partial


class My_class:
    def my_calculator1(self, v1: int = 0, f1: str = '-', v2: int = 0, f2: str = '-',
                       v3: int = 0, f3: str = '-', v4: int = 0, f4: str = '-', v5: int = 0) -> int:
        my_sum = v1
        for f, v in [(f1, v2), (f2, v3), (f3, v4), (f4, v5)]:
            my_sum = eval(str(my_sum) + f + str(v))
        return my_sum

    def my_calculator2(self, v1: int):
        def function1(f1: str):
            def variable2(v2: int):
                def function2(f2: str):
                    def variable3(v3: int):
                        def function3(f3: str):
                            def variable4(v4: int):
                                def function4(f4: str):
                                    def variable5(v5: int) -> int:
                                        my_sum = v1
                                        for f, v in [(f1, v2), (f2, v3), (f3, v4), (f4, v5)]:
                                            my_sum = eval(str(my_sum) + f + str(v))
                                        return my_sum
                                    return variable5
                                return function4
                            return variable4
                        return function3
                    return variable3
                return function2
            return variable2
        return function1


my_obj = My_class()
my_calculator3 = partial(my_obj.my_calculator1, v1=1, v2=2, v3=3, v4=3, v5=2)

print(my_obj.my_calculator1(1, '+', 2, '+', 3, '/', 3, '*', 2))
print(my_obj.my_calculator2(1)('+')(2)('+')(3)('/')(3)('*')(2))
print(my_calculator3(f1='+', f2='+', f3='/', f4='*'))
print(my_calculator3(f1='*', f2='-', f3='-', f4='+'))