from numpy import *

R = random.rand(4, 5)
G = random.randint(2, 100, (4, 5))

print(R.mean())
print(G.mean())
print((R+G).max())
print((R+G).min())