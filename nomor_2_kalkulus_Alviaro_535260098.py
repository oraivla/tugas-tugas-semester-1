
#soal nomor 2
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-5, 5, 100)
y = 9 - x**2

plt.plot(x, y, label="y = 9 - ^2")
plt.grid(True)
plt.legend()


plt.show()