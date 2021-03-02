code = input("주민번호 앞자리 입력:")

y = "20" + code[0:2]
m = code[2:4]
d = code[4:6]

age = 2019 - int(y) + 1
print("당신은", y, "년에 태어났군요.")
print("당신의 생일은", m, "월", d, "일 이군요.")
print("당신은 올해", age, "살 이군요.")