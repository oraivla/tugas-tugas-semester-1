
#soal nomor 3
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-5, 5, 100)
y = x**3

plt.plot(x, y, label="y = x^3")
plt.grid(True)
plt.legend()


plt.show()