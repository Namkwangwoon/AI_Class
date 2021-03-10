def 적정몸무게 (height):
    return (height-100) * 0.9

def BMI (height, weight):
    return weight / (height/100)**2

def 비만도 (bmi) :
    if bmi<20 : return "저체중"
    elif 20 <= bmi <25 : return "정상체중"
    elif 25 <= bmi < 30 : return "경도비만"
    elif 30 <= bmi < 40 : return "비만"
    else : return "고도비만"

height = int(input("키를 입력하세요 : "))
weight = int(input("몸무게를 입력하세요 : "))

bmi = BMI(height, weight)

print("적정몸무게 : %.2f" % 적정몸무게(height))
print("BMI : %.2f" % bmi)
print(비만도(bmi))