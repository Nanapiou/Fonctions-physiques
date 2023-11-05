"""
Nécessite au moins de Python 3.10 pour le match case et 3.8 pour le :=
"""
import matplotlib.pyplot as plt
import numpy as np
from fonctions_utiles import euler # Doesn't work because of folders organization.

R = 1000 # Ohm
L = 10e-3 # H
E = 5 # V
tau = L / R # s
omega = 10 ** 5 # rad.s-1
T = 0.1e-3 # s
k = 1 # Sans dimension

t0, tm = 0, 50e-6 # s

def f_rc(y, t):
    return (E / L) - (1 / tau) * y

def i(t):
    return (E / R) * (1 - np.exp(-R * t / L))

def e(t):
    # return E if isinstance(t, (float, int)) else np.array([E for _ in t])
    return E * np.cos(omega * t)

def e_scie(t):
    return E * (t / T - (t // T))

def e_triangle(t): # Pourquoi ça maarche paaaas
    if isinstance(t, (float, int)):
        return 2 * E * (t - k * T) if k * T <= t <= (k + 0.5) * T else 2 * E * (1 - t + k * T)
    else:
        return np.fromiter(
            (e_triangle(t[i]) for i in range(len(t)))
        , float)

def fosc_rc(y, t):
    return (e(t) / L) - (y / tau)

def f_ur_rc(y, t):
    return (e(t) - y) / tau

# Pour tester bilan de tension
def f_ul_rc(y, t):
    # return (E - (y / tau))
    return (-omega * E * np.sin(omega * t) - (y / tau))

def fscie_rc(y, t):
    return (e_scie(t) / L) - (y / tau)

def fscie_ur_rc(y, t):
    return (e_scie(t) - y) / tau


x = np.linspace(t0, tm, 1000)
plt.title('Circuit RL')

match input("Que faut-il afficher ?\n1 - i(t) résolu analytiquement\n2 - i(t) résolu numériquement\n3 - i(t) résolu numériquement avec une alimentation sinusoidale\n4 - Le bilan de tension en alimentation sinusoidale\n5 - L'amplitude de Ur(t) en fonction de omega\n6 - i(t) résolu numériquement avec une alimentation en scie\n7 - Ur(t) et e(t) avec une alimentation en scie\n8 - L'amplitude de Ur en fonction de T\n9 - Exercice 1, question 7, uc(t), E(t) et u1(t)\n> "):
    case '1':
        plt.xlabel('Temps (s)')
        plt.ylabel('Intensité (A)')
        plt.plot(x, i(x), '-r', label='$i(t)$')
    case '2':
        plt.xlabel('Temps (s)')
        plt.ylabel('Intensité (A)')
        for h, fmt in ((1e-6, '-r'), (1e-7, '-g'), (1e-8, '-b')):
            plt.plot(*euler(f_rc, t0, 0, tm, h), fmt, label=f'$i(t) avec h={h}$')
        plt.plot(x, i(x), '-k', label='$i(t)$')
    case '3':
        plt.xlabel('Temps (s)')
        plt.ylabel('Intensité (A)')
        plt.plot(*euler(fosc_rc, t0, 0, tm, 1e-8), '-b', label='$i(t)$')
    case '4':
        plt.xlabel('Temps (s)')
        plt.ylabel('Tension (V)')

        y_ur = euler(f_ur_rc, t0, 0, tm, (tm - t0) / len(x))[1]
        y_ul = euler(f_ul_rc, t0, E, tm, (tm - t0) / len(x))[1]
        e_vals = e(x)
        plt.plot(x, y_ur, '-m', label='$u_r(t)$')
        plt.plot(x, y_ul, '-y', label='$u_l(t)$')
        plt.plot(x, e_vals, '-c', label='$e(t)$')

        bilan_tensions = np.fromiter((e_vals[i] - y_ur[i] - y_ul[i] for i in range(len(x))), float)
        plt.plot(x, bilan_tensions, '-k', label='$e(t) - u_r(t) - u_l(t)$')
    case '5':
        print("Calcul en cours, veuillez patienter...")
        omaga_vals = np.linspace(1e4, 1e6, 1000)
        amplitudes = np.fromiter(
            (max(ur_vals := (euler(lambda y, t: ((E * np.cos(omega * t) - y) / tau), t0, 0, tm, 1e-8)[1])) - min(ur_vals)
            for omega in omaga_vals)
        , float)
        plt.xlabel('Omega (rad/s)')
        plt.ylabel('Amplitude (V)')
        plt.plot(omaga_vals, amplitudes, '-r', label='Amplitude')
    case '6':
        plt.xlabel('Temps (s)')
        plt.ylabel('Intensité (A)')
        plt.plot(*euler(fscie_rc, t0, 0, tm * 10, 1e-8), '-b', label='$i(t)$')
    case '7':
        plt.xlabel('Temps (s)')
        plt.ylabel('Tension (V)')

        x_allonge = np.linspace(t0, tm * 10, 1000)
        plt.plot(*euler(fscie_ur_rc, t0, 0, tm * 10, 1e-8), '-m', label='$u_r(t)$')
        plt.plot(x_allonge, e_scie(x_allonge), '-c', label='$e(t)$')
    case '8':
        print("Calcul en cours, veuillez patienter...")
        T_vals = np.linspace(1e-6, 1e-3, 1000)
        amplitudes = np.fromiter(
            (max(ur_vals := (euler(lambda y, t: ((E * (t / T - (t // T)) - y) / tau), 1e-4, 0, tm * 10, 1e-8)[1])) - min(ur_vals)
            for T in T_vals)
        , float)
        plt.xlabel('T (s)')
        plt.ylabel('Amplitude (V)')
        plt.plot(T_vals, amplitudes, '-r', label='Amplitude')
        print(f"Non représentatif à partir de T = {tm * 10} s, car la tension n'est plus une scie sur [t0:tm].")
    case '9':
        plt.title("Courbe de $u_c$ pour $t1 < t < t2$")
        alpha = 1/2

        R, C = 1000, 10e-6 # Ohm, F
        tau = R * C # s
        t1 = - tau * np.log(1 - alpha)
        t2 = t1 + tau * np.log((1 + alpha) / (1 - alpha))

        uc = lambda t: E * (-1 + (alpha + 1) * np.exp(-(t - t1) / tau))
        plt.plot(x := np.linspace(t1, t2, 1000), uc(x), '-r', label='$u_c(t)$')
        plt.plot(x, e_vals := np.full(1000, -E), '-b', label='$E(t)$')
        plt.plot(x, e_vals * alpha, '-y', label='$u_1(t)$')
    case _: # Tests
        plt.plot(x := np.linspace(k * T, (k + 1) * T, 1000), e_triangle(x), '-c', label='$E(t)$') # Buh


plt.grid(True)
plt.legend()
plt.show()
