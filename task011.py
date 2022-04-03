class Some_class:
    global glob_var

    def some_metod(self, var2: int = 1, var3: int = 1) -> None:
        # enclosing
        encl_var: int = 2

        def some_metod_in_menod() -> None:
            # local
            loc_var: int = 3
            print(f'sum = {glob_var + encl_var + loc_var}')

        some_metod_in_menod()
        print(f'var2 + var3 = {var2 + var3}')


# global
glob_var: int = 1

sc = Some_class()
sc.some_metod()