#nomor 9
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 1, 400)
y = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x, y)

F = (X + 2)**2 + Y**2 - 4

plt.contour(X, Y, F, [0], colors="blue")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("(x + 2)^2 + y^2 = 4")
plt.grid(True)
plt.gca().set_aspect("equal")

plt.show()