from math import *

import matplotlib.pyplot as plt
import numpy as np


# fonction de tracé d'un rayon

def rayon_sortant(h, color_curve):
    if abs(h) < R / n:
        x_lim_sortant = 3.5
        plt.plot([-1.5, np.abs(np.sqrt(1 - h ** 2))], [h, h], 'k')
        sini = h / R
        i = asin(sini)
        sinr = n * sini
        if abs(sinr - sini) < 0.001:
            plt.plot([-1.5, 3], [h, h], color=color_curve, label='h=' + str(round(h, 1)))
        else:
            r = asin(sinr)
            D = r - i
            pente_rayon_sortant = (-h) / (h / tan(i) + h / tan(D) - np.abs(np.sqrt(1 - h ** 2)))
            ordonnée_origine_rayon_sortant = -pente_rayon_sortant * (h / tan(i) + h / tan(D))
            plt.plot([np.abs(np.sqrt(1 - h ** 2)), x_lim_sortant],
                     [h, pente_rayon_sortant * x_lim_sortant + ordonnée_origine_rayon_sortant], color=color_curve,
                     label='h=' + str(round(h, 1)))
    else:
        plt.plot([-1.5, np.abs(np.sqrt(1 - h ** 2))], [h, h], color=color_curve)
        sini = h / R
        i = asin(sini)
        D = pi - 2 * i
        ylim_ref_tot = h * 0.5
        pente_rayon_sortant = (-h) / (h / tan(D) - np.abs(np.sqrt(1 - h ** 2)))
        ordonnée_origine_rayon_sortant = -pente_rayon_sortant * h / tan(D)
        plt.plot([np.abs(np.sqrt(1 - h ** 2)), (ylim_ref_tot - ordonnée_origine_rayon_sortant) / pente_rayon_sortant],
                 [h, ylim_ref_tot], color=color_curve, label='h=' + str(round(h, 1)))
        print((ylim_ref_tot - ordonnée_origine_rayon_sortant) / pente_rayon_sortant)


# Tracé du graphique

# tracé de la lentille demi-boule

n = 3/2
R = 1

plt.plot([0, 0], [-1, 1], color='black')

dioptre_y = np.linspace(-1, 1, 1000)
dioptre_x = np.abs(np.sqrt(1 - dioptre_y ** 2))
plt.plot(dioptre_x, dioptre_y, color='black')

# Tracé d'un grain du capteur en gris sur le graphique

x_c = 3
d_c = 0.2
plt.plot([x_c, x_c], [-d_c / 2, d_c / 2], color='0.5')

plt.plot([-10, 20], [0, 0], '--k', lw=0.5)

# Tracé du rayon

h = 2 / 3 - 0.1

rayon_sortant(h, 'black')

# Affichage de la figure

plt.legend(bbox_to_anchor=(1.05, 1))
plt.axis((-1, 3.5, -2.5, 2.5))
plt.gca().set_aspect("equal", adjustable="box")
plt.title('Lentille demi-boule d\'indice n=' + str(n))
plt.show()
