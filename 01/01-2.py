str1 = input("문자열1 : ")
str2 = input("문자열2 : ")
str = "/".join(str1[1::2]+str2[::2])
print(str)