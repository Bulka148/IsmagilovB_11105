class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def _sravn(self, other):
        # сравнение успеваемости учеников
        g, o = self.grades, other.grades
        score = g.count(5) * 10 + g.count(4) * 5 + g.count(3) - g.count(2) * 8
        score_other = o.count(5) * 10 + o.count(4) * 5 + o.count(3) - o.count(2) * 8
        return (score, score_other)

    def __lt__(self, other):
        score, score_other = self._sravn(other)
        return score < score_other

    def __gt__(self, other):
        score, score_other = self._sravn(other)
        return score > score_other

    def __le__(self, other):
        score, score_other = self._sravn(other)
        return score <= score_other

    def __ge__(self, other):
        score, score_other = self._sravn(other)
        return score >= score_other

    def __eq__(self, other):
        score, score_other = self._sravn(other)
        return score == score_other

    def __ne__(self, other):
        score, score_other = self._sravn(other)
        return score != score_other


stud1 = Student('Vova', [5, 4, 5, 2, 4])
stud2 = Student('Petya', [2, 2, 3, 2, 3])
stud3 = Student('Vitya', [2, 5, 5, 4, 4])

print(stud1 != stud3)