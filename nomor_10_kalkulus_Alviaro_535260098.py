#nomor 10
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 8, 400)
y = np.linspace(-4, 6, 400)
X, Y = np.meshgrid(x, y)

F = (X - 3)**2 + (Y - 1)**2 - 16

plt.contour(X, Y, F, [0], colors="blue")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("(x - 3)^2 + (y - 1)^2 = 16")
plt.grid(True)
plt.gca().set_aspect("equal")

plt.show()