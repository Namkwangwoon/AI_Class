class Employee:

    def __init__(self, f_name, l_name, age, pay):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        self.pay = pay

    def info(self):
        print("%s %s님의 나이는 %d입니다.\n" % (self.first_name, self.last_name, self.age))

    def get_pay(self):
        print("%s %s님의 현재 연봉은 %d만원 입니다.\n" % (self.first_name, self.last_name, self.pay))

    def apply_raise(self, raise_amount):
        while raise_amount < 1:
            print("[경고] 인상률은 1보다 작을 수 없습니다.")
            raise_amount = float(input("인상률을 압력해 주세요 : "))

        new_pay = self.pay + (self.pay * (raise_amount/100))
        print("%s %s님의 연봉은 %1.f%%인상률을 적용하여 %d만원입니다.\n" % (self.first_name, self.last_name, raise_amount, new_pay))

emp_1 = Employee('Sanghee', 'Lee', 35, 4000)
emp_2 = Employee('Minjung', 'Kim', 40, 6000)

emp_1.info()
emp_1.get_pay()

emp_2.info()
emp_2.get_pay()

emp_1.apply_raise(3)

emp_2.apply_raise(-1)