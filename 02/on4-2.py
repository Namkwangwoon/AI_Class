class SoccerPlayer:
    name = ""
    position = ""
    number = None

    def __init__(self, na, p, nu):
        self.name = na
        self.position = p
        self.number = nu

    def getInfo(self):
        print(self.name, self.position, self.number)

    def setNumber(self, n):
        self.number = n

HmSon = SoccerPlayer("손흥민", "FW", 40)

print("현재 선수의 등번호는 : ", HmSon.number)
HmSon.setNumber(7)
print("현재 선수의 등번호는 : ", HmSon.number)
HmSon.getInfo()