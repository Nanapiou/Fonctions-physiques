import numpy as np
from numpy.random import *  # ici, on charge numpy.random pour pouvoir créer un tableau de valeurs aléatoires

E0, u_E0 = 8.7, 0.04
R, u_R = 985e3, 14e3 / np.sqrt(3)
C, u_C = 1.035e-6, 44e-9 / np.sqrt(3)
t, u_t = 2.7, 0.025 / np.sqrt(3)
Nsim = 50000
E0_sim = uniform(E0 - u_E0 * np.sqrt(3), E0 + u_E0 * np.sqrt(3), Nsim)
R_sim = uniform(R - u_R * np.sqrt(3), R + u_R * np.sqrt(3), Nsim)
C_sim = uniform(C - u_C * np.sqrt(3), C + u_C * np.sqrt(3), Nsim)
t_sim = uniform(t - u_t * np.sqrt(3), t + u_t * np.sqrt(3), Nsim)


def tension(E0, t, R, C):  # Definition de la fonction
    return E0 * np.exp(-t * R * C)


tension_sim = tension(E0_sim, t_sim, R_sim, C_sim)
# On appelle la fonction, avec comme arguments nos arrays de simulation
tension_moy = np.mean(tension_sim)
tension_ecartType = np.std(tension_sim)
print('Moyenne = {:.3e} / Écart-type = {:.1e}'.format(tension_moy, tension_ecartType))
# Affichage des resultats
