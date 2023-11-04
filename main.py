"""
DM2 pasted
"""
import matplotlib.pyplot as plt
import numpy as np
from math import cos
import scipy.integrate as integrate
from fonctions_utiles import euler # Doesn't work because of folders organization.

R = 1000 # Ohm
L = 10e-3 # H
E = 5 # V
tau = L / R # s
omega = 10 ** 5 # rad.s-1

t0, tm = 0, 50e-6 # s

def f_rc(y, t):
    return (E / L) - (1 / tau) * y

def i(t):
    return (E/R)*(1 - np.exp(-R*t/L))

def e(t):
    # If is array, return array of E, else return E
    # return E if isinstance(t, (float, int)) else np.array([E for _ in t])
    return E * np.cos(omega * t)

def fosc_rc(y, t):
    return (e(t) / L) - (y / tau)

def f_ur_rc(y, t):
    return (e(t) - y) / tau

# Pour tester bilan de tension
def f_ul_rc(y, t):
    return (-omega * E * np.sin(omega * t) - (y / tau))


x = np.linspace(t0, tm, 1000)

match input("Que faut-il afficher ?\n1 - i(t) résolu analytiquement\n2 - i(t) résolu numériquement\n3 - i(t) résolu numériquement avec une alimentation sinusoidale\n4 - Le bilan de tension en alimentation sinusoidale\n> "):
    case '1':
        plt.xlabel('Temps (s)')
        plt.ylabel('Intensité (A)')
        plt.plot(x, i(x), '-r', label='i(t)')
    case '2':
        plt.xlabel('Temps (s)')
        plt.ylabel('Intensité (A)')
        for h, fmt in ((1e-6, '-r'), (1e-7, '-g'), (1e-8, '-b')):
            plt.plot(*euler(f_rc, t0, 0, tm, h), fmt, label=f'i(t) avec h={h}')
        plt.plot(x, i(x), '-k', label='i(t)')
    case '3':
        plt.xlabel('Temps (s)')
        plt.ylabel('Intensité (A)')
        plt.plot(*euler(fosc_rc, t0, 0, tm, 1e-8), '-b', label='i(t)')
    case '4':
        plt.xlabel('Temps (s)')
        plt.ylabel('Tension (V)')

        y_ur = euler(f_ur_rc, t0, 0, tm, (tm - t0) / len(x))[1]
        y_ul = euler(f_ul_rc, t0, E, tm, (tm - t0) / len(x))[1]
        plt.plot(x, y_ur, '-m', label='Ur')
        plt.plot(x, y_ul, '-y', label='Ul')
        plt.plot(x, e_vals := e(x), '-c', label='e(t)')

        bilan_tensions = list()
        for i in range(len(x)):
            bilan_tensions.append(e_vals[i] - y_ur[i] - y_ul[i])
        plt.plot(x, bilan_tensions, '-k', label='e - uR - uL')

plt.title('Circuit RL')
plt.grid(True)
plt.legend()
plt.show()
