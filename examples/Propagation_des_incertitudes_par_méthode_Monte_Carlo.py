#Bibliothèques
import random as rd
import numpy as np
from math import *
import matplotlib.pyplot as plt

#valeur de x

x=10 
u_x = 0.5

#Calcul de l'incertitude sur y=sqrt(x)

N=10000 #nb d'évaluations Monte Carlo

liste_y=[]

for i in range(N):
  x_MC=x+rd.uniform(-1,1)*sqrt(3)*u_x #tirage aléatoire de x_MC dans la précision sur x (taille de la graduation = incertitude*sqrt(3) si distribution uniforme)
  y_MC=sqrt(x_MC)
  liste_y.append(y_MC)

ymoy=np.mean(liste_y)
u_y=np.std(liste_y,ddof=1)

print('y= {:.3e} +/- {:.1e} unité'.format(ymoy,u_y))

#Tracé de l'histogramme des valeurs de y 

plt.hist(liste_y,bins='rice') 
plt.xlabel('valeur de y')
plt.show()

