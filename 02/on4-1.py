class Circle:

    radius = None
    
    def __init__(self, r):
        print("Circle 객체가 생성됩니다.")
        self.radius = r

    def setR(self, r):
        self.radius = r

    def 넓이구하기(self):
        area = self.radius * self.radius * 3.14
        print("원의 넓이는 %.2f" % area)

    def 둘레구하기(self):
        line = 2 * self.radius * 3.14
        print("원의 둘레는 %.2f" % line)


c1 = Circle(20)
print("c1의 반지름은", c1.radius)
c1.setR(10)
print("c1의 반지름은", c1.radius)
c1.넓이구하기()
c1.둘레구하기()