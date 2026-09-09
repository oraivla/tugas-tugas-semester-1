
#soal nomor 1
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-5, 5, 100)
y = 4 * x

plt.plot(x, y, label="y = 4 * x")
plt.grid(True)
plt.legend()


plt.show()