#!/usr/bin/env python
# coding: utf-8

# **Exemple de code permettant de réaliser une régression linéaire et d'obtenir les incertitudes sur les coefficients de régression.**

# In[ ]:


import matplotlib.pyplot as plt
# Bibliothèques
import numpy as np

# In[ ]:


# valeurs de y

y = np.array([2.40, 1.69, 0.91, 0.57, 0.35])

u_y = 0.05

# valeurs de x

x = np.array([1.18, 1.01, 0.82, 0.74, 0.69])

u_x = np.array([0.0023, 0.0017, 0.0011, 0.0009, 0.0008])

# In[ ]:


# Tracé des données avec les barres d'erreur
plt.figure(figsize=(8, 6))
plt.xlabel('x')
plt.ylabel('y')

plt.errorbar(x, y, xerr=u_x, yerr=u_y, fmt='b+', zorder=2, label='Données')
plt.legend()
plt.show()

# In[ ]:


# Ajustement des données par une fonction affine
p = np.polyfit(x, y, 1)
a = p[0]  # pente de la droite d'ajustement
b = p[1]  # ordonnée à l'origine de la droite d'ajustement

# Tracé des données avec la droite d'ajustement
plt.figure(figsize=(8, 6))
plt.xlabel('x')
plt.ylabel('y')

xfit = np.linspace(min(x), max(x), 2)

plt.plot(xfit, b + a * xfit, 'r', label='Régression linéaire')
plt.errorbar(x, y, xerr=u_x, yerr=u_y, fmt='b+', zorder=2, label='Données')
plt.legend()
plt.show()

# In[ ]:


# Vérification de la validité de la régression linéaire avec les résidus
plt.subplot(211)
res = (y - np.polyval(p, x))  # Résidus
plt.plot(x, res, 'ro')  # Tracé des résidus
plt.errorbar(x, res, yerr=u_y, fmt='r+', zorder=2, label='Mesures')
plt.grid(True)
plt.ylabel('résidus')
plt.xlabel('x')
plt.subplot(212)
z = (y - np.polyval(p, x)) / u_y  # Résidus normalisés
plt.plot(x, z, 'ro')  # Tracé des résidus normalisés, |z| reste <2 donc la régression linéaire est validée
plt.grid(True)
plt.ylabel('résidus normalisés')
plt.xlabel('x')
plt.show()

# 1. sur les résidus : la valeur 0 est bien dans les barres d'erreurs -> ajustement validé
# 2. sur les résidus normalisés : z<2 pour tous les points -> ajustement validé


# In[ ]:


# Détermination des incertitudes sur les paramètres de modélisation par méthode Monte-Carlo
N = 1000

ta = []  # liste qui contiendra les valeurs de pente
tb = []  # liste qui contiendra les valeurs d'ordonnée à l'origine

for i in range(0, N):
    l = len(x)
    my = y + u_y * np.sqrt(3) * np.random.uniform(-1, 1,
                                                  l)  # le sqrt(3) vient du fait qu'on prend une distribution uniforme sur la graduation de y / tirage de y
    mx = x + u_x * np.sqrt(3) * np.random.uniform(-1, 1,
                                                  l)  # le sqrt(3) vient du fait qu'on prend une distribution uniforme sur la graduation de x / tirage de x
    p_MC = np.polyfit(mx, my, 1)  # Ajustement après tirage aléatoire en chaque point
    ta.append(p_MC[0])
    tb.append(p_MC[1])

u_a = np.std(ta, ddof=1)  # incertitude sur la pente
u_b = np.std(tb, ddof=1)  # incertitude sur l'ordonnée à l'origine

print('a= {:.3e} +/- {:.1e} unité'.format(a, u_a), 'et b={:.3e} +/- {:.1e} unité'.format(b, u_b))

# In[ ]:
