'''Appel des bibliothèques'''
import matplotlib.pyplot as plt
# rendre les graphiques moins flous
import matplotlib_inline.backend_inline as bckend
import numpy as np
from numpy.random import *

bckend.set_matplotlib_formats('svg')

'''Saisie des données'''
# Angle d'incidence
i1 = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
Delta_i1 = 0.5
# Angle de réfraction
i2 = np.array([0, 3, 7, 10, 13, 16, 19.5, 22.5, 25, 28, 31, 33, 35, 37, 39, 40, 41, 41.5])
Delta_i2 = 1

'''Calcul des sinus'''
sini1 = np.sin(np.radians(i1))
sini2 = np.sin(np.radians(i2))

'''Incertitudes sur les sinus'''
Nsim = 5000
u_sini1 = []
u_sini2 = []
for i in range(len(i1)):
    i1_sim = uniform(i1[i] - Delta_i1, i1[i] + Delta_i1, Nsim)
    i2_sim = uniform(i2[i] - Delta_i2, i2[i] + Delta_i2, Nsim)
    sini1_sim = np.sin(np.radians(i1_sim))
    sini2_sim = np.sin(np.radians(i2_sim))
    u_sini1.append(np.std(sini1_sim))
    u_sini2.append(np.std(sini2_sim))

'''Calcul de la régression linéaire'''
# Ajustement des données par une fonction affine
p = np.polyfit(sini1, sini2, 1)
a = p[0]  # pente de la droite d'ajustement
b = p[1]  # ordonnée à l'origine de la droite d'ajustement

'''Incertitudes sur la régression linéaire'''
a_sim = []
b_sim = []
for i in range(Nsim):
    sini1_sim_u = []
    sini2_sim_u = []
    for j in range(len(i1)):
        sini1_sim_u.append(uniform(sini1[j] - u_sini1[j] * np.sqrt(3),
                                   sini1[j] + u_sini1[j] * np.sqrt(3)))
        sini2_sim_u.append(uniform(sini2[j] - u_sini2[j] * np.sqrt(3),
                                   sini2[j] + u_sini2[j] * np.sqrt(3)))
    a, b = np.polyfit(sini1_sim_u, sini2_sim_u, 1)
    a_sim.append(a)
    b_sim.append(b)
u_a = np.std(a_sim)
u_b = np.std(b_sim)

'''Définition de la figure'''
plt.figure(figsize=(8, 6))
plt.xlabel('$\sin(i_1)$')
plt.ylabel('$\sin(i_2)$')

'''Tracé des points expérimentaux'''
plt.errorbar(sini1, sini2, xerr=u_sini1, yerr=u_sini2, marker='none',
             linestyle='none', lw=1, zorder=2, label='Données')

'''Tracé de la régression linéaire'''
xfit = np.linspace(min(sini1), max(sini1), 2)
plt.plot(xfit, b + a * xfit, 'r', lw=0.5,
         label='y=(' + str(round(a, 3)) + '$\pm$' + str(round(u_a, 3)) + ')$\cdot$x+('
               + str(round(b, 3)) + '$\pm$' + str(round(u_b, 3)) + ')')

'''Affichage de la figure'''
plt.legend()
plt.show()
