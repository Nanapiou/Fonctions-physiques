import matplotlib.pyplot as plt
import numpy as np
from fonctions_utiles import euler # Doesn't work because of folders organization.

R = 1000 # Ohm
L = .01 # H
E = 5 # V
tau = L / R

t0, tm = 0, 50e-6

def f_rc(y):
    return (E / L) - (1 / tau) * y

def i(t):
    return (E/R)*(1 - np.exp(-R*t/L))


fig = plt.figure()
plt.title('RL Circuit')
plt.xlabel('Time (micro-s)')
plt.ylabel('Current (A)')
plt.grid(True)

for h, fmt in ((1e-6, '-r'), (1e-7, '-g'), (1e-8, '-b')):
    plt.plot(*euler(f_rc, t0, 0, tm, h), fmt)

x = np.linspace(0, 50e-6, 1000)
plt.plot(x, i(x), '-k')
plt.show()
