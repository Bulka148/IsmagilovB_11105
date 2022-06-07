class Plant:
    glb = 'Plant'

    def __init__(self, name: str = None):
        self.name = name

    @classmethod
    def is_predator(cls, name=None):
        if name == None:
            print(cls.glb + ' Is a herbivore')
        else:
            print(cls.glb + ' Is a predator')

    @staticmethod
    def foo(age):
        print('I am', age, 'years old')

    def my_name(self):
        if self.name == None:
            print(self.glb +'. ' + ' I am unknown ')
        else:
            print(self.glb + '. ' + 'My name is ' + self.name)


myAnimal = Plant('Rose')
myAnimal.is_predator(myAnimal.name)
Plant.is_predator('Rose_classic')
Plant.foo(7)