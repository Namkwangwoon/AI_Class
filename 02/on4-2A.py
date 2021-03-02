class SoccerPlayer:

    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("선수의 등번호를 변경한다 : From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number

    def get_info(self):
        print("Hello, my name is %s. I play in %s in center." % (self.name, self.position))


HmSon = SoccerPlayer("손흥민", "FW", 40)

print("현재 선수의 등번호는 : ", HmSon.back_number)
HmSon.change_back_number(7)
print("현재 선수의 등번호는 : ", HmSon.back_number)
HmSon.get_info()