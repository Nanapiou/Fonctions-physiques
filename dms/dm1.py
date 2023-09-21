"""
Dessiner la distance focale en fonction de la hauteur
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("svg")

R, n = 1, 3 / 2
hl = R / n
x = np.arange(0.1 * R, hl, 0.001)
y = x / np.tan(i1 := x / R) + x / np.tan(np.arcsin((x * n) / R) - i1)

plt.plot(x, y, "b")
plt.savefig("output.svg", format="svg")
