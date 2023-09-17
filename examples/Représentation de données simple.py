#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Bibliothèques
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#valeurs de y

y=np.array([2.40,1.69,0.91,0.57,0.35])

#valeurs de x

x=np.array([1.18, 1.01, 0.82, 0.74, 0.69])


# In[4]:


#Tracé des données avec les barres d'erreur
plt.figure(figsize=(8,6))
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x, y,'b+')
plt.show()


# In[ ]:




