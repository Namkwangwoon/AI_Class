class Student:

    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

    def getSum(self):
        return self.korean + self.english + self.math

    def getAverage(self):
        return self.getSum()/3

std1 = Student("kim", 90, 80, 75)
print(std1.getSum())
print(std1.getAverage())