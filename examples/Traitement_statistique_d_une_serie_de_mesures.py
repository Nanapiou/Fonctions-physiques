# Bibliothèques
import numpy as np

x = np.array([198., 203., 195., 204., 199., 203., 196., 202., 201., 196.])  # mesures

xmoy = np.mean(x)
u_x = np.std(x, ddof=1) / np.sqrt(
    len(x))  # on oublie pas de diviser par la racine du nombre de mesure lors une évaluation statistique

print('x= {:.3e} +/- {:.1e} unité'.format(xmoy, u_x))
