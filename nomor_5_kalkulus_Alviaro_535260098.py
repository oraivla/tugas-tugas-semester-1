#soal nomor 5
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-5, 5, 100)
y = np.cos(2 * x)

plt.plot(x, y, label="y = cos (2x)")
plt.grid(True)
plt.legend()


plt.show()