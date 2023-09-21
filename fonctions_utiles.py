"""
Des fonctions usuelles utiles
"""
from random import uniform


def monte_carlo(fn, *args, N=5000):
    """
    Une version généralisée de monte-carlo

    Exemple d'utilisation:
        result = list(monte_carlo(lambda a, b: sin(a) * sin(b), (3, 0.5), (5, 0.3)))
    Ici, a vaudra 3 +/- 0.5 et b vaudra 5 +/- 0.3
    Un générateur de toutes les valeurs résultantes sera retourné

    :param: fn Une fonction, qui utilisera les paramètres (simulés)
    :param: *args Une suite d'argument de la forme (valeur, delta), qui seront utilisés dans le même ordre dans la fonction
    :param: N Le nombre de simulation par argument
    :return: Generator Un itérateur des résultats
    """
    yield from (fn(*(uniform(e - delta, e + delta) for e, delta in args)) for i in range(N))


if __name__ == "__main__":
    import numpy as np

    array = np.fromiter(
        monte_carlo(lambda x1, x2, D: ((D ** 2) - ((x2 - x1) ** 2)) / (4 * D), (18, 3), (41, 3), (60, 0.1)),
        float
    )

    print("Distance focale: %.2f +/- %.2f cm" % (np.mean(array), np.std(array)))
