import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

cctvs = [540000, 320000, 600000, 520000, 370000, 540000, 360000, 410000, 380000, 320000, 240000, 480000, 160000, 130000, 400000]
population = [3200, 800, 900, 2000, 800, 1500, 1800, 1300, 900, 1200, 2000, 2100, 1600, 1000, 900]
plt.scatter(cctvs, population)
plt.xlabel('CCTV 수')
plt.ylabel('인구 수')
plt.title('자치구의 인구 수와 CCTV 수의 관계')
plt.grid(True)
plt.show()