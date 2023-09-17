from random import *


def test_position(x, y, f, g):
    if y < f(x) and y > g(x):
        return True
    else:
        return False


### Les fonctions ###
f = lambda x: 4 * x / (x ** 2 + 1)
g = lambda x: x * (x - 1.2)

### Les variables ###
compteur = 0
N = 100000

### Le corps du programme ###
for i in range(N):
    x = uniform(0, 2)
    y = uniform(-0.5, 2)
    if test_position(x, y, f, g):
        compteur += 1
print('le compteur:', compteur)
print('aire approximative :', compteur / N * 5)
