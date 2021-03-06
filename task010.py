import abc


class Drink:
    def __init__(self, names):
        self.names = names

    def __iter__(self):
        return iter(self.names)

class Classic_drink(abc.ABC):
    @abc.abstractmethod
    def step1(self):
        pass

    @abc.abstractmethod
    def step2(self):
        pass

    @abc.abstractmethod
    def step3(self):
        pass

    @abc.abstractmethod
    def step4(self):
        pass

    @abc.abstractmethod
    def step5(self):
        pass

class Tea(Classic_drink):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def step1(self):
        pass
    def step2(self):
        pass
    def step3(self):
        pass
    def step4(self):
        pass
    def step5(self):
        pass
    def step6(self):
        pass
    def step7(self):
        pass


class Coffee(Classic_drink):
    def step1(self):
        pass
    def step2(self):
        pass
    def step3(self):
        pass
    def step4(self):
        pass
    def step5(self):
        pass
    def step8(self):
        pass
    def step9(self):
        pass
    def step10(self):
        pass