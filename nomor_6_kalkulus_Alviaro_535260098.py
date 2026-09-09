#soal nomor 6
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-1, 1, 100)
y = np.arcsin(x)

plt.plot(x, y, label="y = arc sin(x)")
plt.grid(True)
plt.legend()


plt.show()