class Employee:

    def __init__(self, first_name='', last_name='', age=0, pay=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.pay = pay

    def info(self):
        print("이름 : %s,  나이 : %d" % (self.last_name+" "+self.first_name, self.age))

    def get_pay(self):
        print("현재 연봉 : %d" % (self.pay))

    def apply_raise(self, raise_amount):
        print("인상된 연봉 : %d" % (self.pay * (1+raise_amount/100)))

emp_1 = Employee('Sanghee', 'Lee', 35, 4000)
emp_2 = Employee('Minjung', 'Kim', 40, 6000)

emp_1.info()
emp_1.get_pay()

emp_2.info()
emp_2.get_pay()

emp_1.apply_raise(3)

emp_2.apply_raise(-1)