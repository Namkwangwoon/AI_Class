import numpy as np

R = np.random.rand(4, 5)
G = np.random.randint(2, 100, size=(4, 5))

print("R의 평균:", R.mean())
print("G의 평균:", G.mean())
print("R과 G의 합의 최대값:", (R+G).max())
print("R과 G의 합의 최소값:", (R+G).min())