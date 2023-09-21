"""
Dessiner la distance focale en fonction de la hauteur
"""
from math import asin

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("svg")

R, n = 1, 3 / 2
hl = R / n
x = np.arange(0.01 * R, hl, 0.001)
y = x / np.tan(i1 := x / R) + x / np.tan(np.arcsin((x * n) / R) - i1)

plt.plot(x, y, "b")
plt.title("Distance focale de la lentille en fonction de la hauteur du rayon")
plt.xlabel("h")
plt.ylabel("f'")
plt.savefig("output.svg", format="svg")

h = 1.
for h in x:
    if h > hl:
        continue
    D = asin(h / R) + asin((h * n) / R)
    if D > 1:
        break

print("Hauteur limite pour être dans les conditions de Gauss: %.3f cm" % h)
