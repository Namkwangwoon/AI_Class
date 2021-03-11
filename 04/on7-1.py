import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 1)
y1 = x
y2 = x + 1
y3 = x + 2
y4 = x + 3

plt.plot(x, y1, '>--r', x, y2, 's-g', x, y3, 'D:b', x, y4, 'x-.c')
# plt.xlim(0, 5)
# plt.ylim(0, 8)
plt.xlabel('X축')
plt.ylabel('Y축')
plt.title('그래프 제목')
plt.grid('True')
plt.legend(['data1', 'data2', 'data3', 'data4'], loc = 'lower right')
plt.show()