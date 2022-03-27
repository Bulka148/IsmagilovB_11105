class Animal:
    num_animals = 0

    def __init__(self, name):
        self.name = name
        Animal.num_animals += 1

    def get_name(self):
        return self.name

    def get_num_animals(self=None):
        return Animal.num_animals

    @staticmethod
    def stutic_metod():
        print('Who am I?')


slon = Animal('slon')
print(slon.get_name())
print(slon.get_num_animals())
print(Animal.get_num_animals())
Animal.stutic_metod()