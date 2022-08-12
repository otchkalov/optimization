"""
Object function calculation
"""
import numpy as np


def func(x, ofname=" "):
    # Calculate object function value
    if ofname == "quadratic":
        of = (x[0] - 1) ** 2 + (x[1] - 1) ** 2 - x[0] * x[1]
    # of = (x[0] - 1)**2 + (x[1] - 1)**2
    # of = fun + np.random.uniform(-1, 1)
    elif ofname == "Himmelblau":
        of = (x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2
    elif ofname == "Rastrigin":
        of = (
            x[0] ** 2
            + x[1] ** 2
            - 10 * (2 - np.cos(2 * np.pi * x[0]) - np.cos(2 * np.pi * x[1]))
        )
    elif ofname == "Rosenbrock":
        of = 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2
    elif ofname == "Ackley":
        of = (
            -20 * np.exp(-0.2 * np.sqrt(0.5 * (x[0] ** 2 + x[1] ** 2)))
            - np.exp(0.5 * (np.cos(2 * np.pi * x[0]) + np.cos(2 * np.pi * x[1])))
            + np.e
            + 20
        )
    else:
        of = 0
    return of


def set_limits(func_name):
    switcher = {
        "quadratic": [[-4, 4], [-4, 4]],
        "Himmelblau": [[-5, 5], [-5, 5]],
        "Rasstrigin": [[-1, 1], [-1, 1]],
        "Rosenbrock": [[-2, 2], [-1, 3]],
        "Ackley": [[-4, 4], [-4, 4]],
    }
    limits = switcher.get(func_name, [[0, 0], [1, 1]])
    return limits[0], limits[1]
