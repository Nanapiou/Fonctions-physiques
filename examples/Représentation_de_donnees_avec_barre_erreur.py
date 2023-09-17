#Bibliothèques
import numpy as np
import matplotlib.pyplot as plt

#valeurs de y

y=np.array([2.40,1.69,0.91,0.57,0.35])

u_y=0.05

#valeurs de x

x=np.array([1.18, 1.01, 0.82, 0.74, 0.69])

u_x=np.array([0.0023, 0.0017, 0.0011, 0.0009, 0.0008])


#Tracé des données avec les barres d'erreur
plt.figure(figsize=(8,6))
plt.xlabel('x')
plt.ylabel('y')

plt.errorbar(x, y,xerr=u_x ,yerr=u_y,fmt='b+',zorder=2,label='Données')
plt.legend()
plt.show()