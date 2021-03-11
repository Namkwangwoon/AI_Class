import matplotlib.pyplot as plt
import numpy as np

age = np.arange(10, 110, 10)
male = [5200, 5200, 11500, 10800, 10000, 8790, 6370, 3760, 1050, 20]
female = [5800, 5400, 10500, 11200, 10000, 10010, 6930, 4040, 1550, 370]
plt.bar(age, male, color='b', align='edge', width=3)
plt.bar(age+3, female, color='r', align='edge', width=3, tick_label=age)
plt.xlabel('연령')
plt.ylabel('인구')
plt.title('동작구 상도동의 인구구조')
plt.legend(['남', '여'], loc='upper right')
plt.show()