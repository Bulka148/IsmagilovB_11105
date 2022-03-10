from abc import ABC, abstractmethod

class Institut:
    def __init__(self, name, surname, group, score):
        self.name = name
        self.surname = surname
        self.group = group
        self.score = score
    def Dopka(self):
        if self.score > 56:
            return 'dopka'
        else:
            return 'ok'

class Unik(Institut):
    def __init__(self, name, surname, group, score, dopscore):
        super(Unik, self).__init__(name, surname, group, score)
        self.dopscore = dopscore

    def DopUpScore(self):
        if self.dopscore == 0:
            return self.score
        else:
            return self.score + self.dopscore

    def Magistratura(self):
        if self.group > 50:
            return 'Magistr'
        else:
            return 'Bakalavr'

    def SpisokStudentsAllTime(self):
        [str(self.surname), ' ', str(self.name)]

class TopUnik(Institut):
    def __init__(self, name, surname, group, score, olimpiadascore):
        super(Unik, self).__init__(name, surname, group, score)
        self.olimpiadascore = olimpiadascore

    def GoodOrNot(self):
        if self.olimpiadascore > 70:
            return 'GOOD, prinyat'
        else:
            return 'Nope'

