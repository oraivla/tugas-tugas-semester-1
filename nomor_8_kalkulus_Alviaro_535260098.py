#soal nomor 8
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 4, 100)
y = np.exp(-x)

plt.plot(x, y, label="y = e^(-x)")
plt.grid(True)
plt.legend()

plt.show()