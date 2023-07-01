import numpy as np
import math
import matplotlib.pyplot as plt

n = 4
xi = 0.3

def F(m):
    return bin(m).count('1')

def C(n, k):
    return math.perm(n, k) // math.factorial(k)

fig, ax = plt.subplots()

ax.set_title(f"xi = {xi}")
ax.set_ylabel("k")
ax.set_xlabel("q(k;xi)")

omegas = np.arange(n+1)
labels = list(range(n+1))

table = np.zeros((n+1,2**n))
for k in range(n+1):
    p = xi**k * (1.-xi)**(n-k)
    table[k] = np.array([p]*C(n, k) + [0.]*(2**n - C(n, k)))
table = table.transpose()

for i in range(2**n):
    ax.barh(omegas, table[i], left=table[:i].sum(axis=0))

plt.show()