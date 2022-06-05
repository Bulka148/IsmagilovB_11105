class Brand:
    def __init__(self, name: str):
        self.name = name

    def print_name(self):
        print(self.name)


class Car:
    def __init__(self, element: list):
        self.element = element

    def __iter__(self):
        return iter(self.element)


if __name__ == '__main__':
    brand_1 = Brand('Cayenne')
    brand_2 = Brand('Macan')
    brand_3 = Brand('Panamera')
    Porshe = Car([brand_1, brand_2, brand_3])
    for i in Porshe:
        i.print_name()