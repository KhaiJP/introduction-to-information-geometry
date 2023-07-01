import numpy as np
import matplotlib.pyplot as plt

n = 4
xi = 0.3

def F(m):
    return bin(m).count('1')

fig, ax = plt.subplots()

ax.set_title(f"xi = {xi}")
ax.set_ylabel("m")
ax.set_xlabel("p(m;xi)")

omegas = np.arange(2**n)
labels = list(range(2**n))
ps = np.array([xi**F(m) * (1.-xi)**(n-F(m)) for m in range(2**n)])

plt.barh(omegas, ps, tick_label=labels, color='gray')
plt.show()