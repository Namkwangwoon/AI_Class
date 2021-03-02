class Student:
    name = None
    kor = None
    eng = None
    mat = None

    def __init__(self, name='', kor=0, eng=0, mat=0):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def getSum(self):
        sum = self.kor + self.eng + self.mat
        return sum

    def getAve(self):
        ave = self.getSum() / 3
        return ave

std1 = Student("kim", 90, 80, 75)
print(std1.getSum())
print(std1.getAve())