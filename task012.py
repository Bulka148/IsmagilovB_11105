from functools import partial


class Some_class:
    def calc(self,
             var1: int = 0, opr1: str = '+',
             var2: int = 0, opr2: str = '+',
             var3: int = 0, opr3: str = '+',
             var4: int = 0, opr4: str = '+',
             var5: int = 0) -> int:
        logic = {'+': lambda a, b: a + b,
                 '-': lambda a, b: a - b,
                 '*': lambda a, b: a * b,
                 '/': lambda a, b: a / b}
        return logic[opr4](logic[opr3](logic[opr2](logic[opr1](var1, var2), var3), var4), var5)

    def spec_calc(self, var1: int):
        def opr_1(opr1: str):
            def var_2(var2: int):
                def opr_2(opr2: str):
                    def var_3(var3: int):
                        def opr_3(opr3: str):
                            def var_4(var4: int):
                                def opr_4(opr4: str):
                                    def var_5(var5: int) -> int:
                                        logic = {'+': lambda a, b: a + b,
                                                 '-': lambda a, b: a - b,
                                                 '*': lambda a, b: a * b,
                                                 '/': lambda a, b: a / b}
                                        return logic[opr4](logic[opr3](logic[opr2](logic[opr1](var1, var2),
                                                                                   var3), var4), var5)
                                    return var_5
                                return opr_4
                            return var_4
                        return opr_3
                    return var_3
                return opr_2
            return var_2
        return opr_1


sc = Some_class()
print(sc.calc(1, '+', 2, '-', 3, '+', 4, '*', 5))
print(sc.spec_calc(1)('*')(2)('+')(3)('-')(4)('+')(5))

calc_par = partial(sc.calc, var1=1, var2=2, var3=3, var4=4, var5=5)
print('(((1+2)+3)*4)+5 =', calc_par(opr1='+', opr2='+', opr3='*', opr4='+'))
print('(((1*2)+3)-4)/5 =', calc_par(opr1='*', opr2='+', opr3='-', opr4='/'))
print('(((1-2)-3)*4)*5 =', calc_par(opr1='-', opr2='-', opr3='*', opr4='*'))