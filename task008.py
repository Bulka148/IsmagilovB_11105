class Drink:
    def __init__(self, names):
        self.names = names

    def __iter__(self):
        return iter(self.names)


class Tea:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


teas = [Tea('green'), Tea('black'), Tea('red'), Tea('yellow')]
drinks = Drink(teas)

for drink in drinks:
    print(drink.get_name())