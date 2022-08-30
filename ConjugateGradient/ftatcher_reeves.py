"""
Conjugate gradient method
"""
import gold_section as gs
# import plotter
import numpy as np


def func(x):
    # Calculate object function value

    # Simple quadratic function
    # fun = (x[0] - 1) ** 2 + (x[1] - 1) ** 2 - x[0] * x[1]
    # fun = (x[0] - 1)**2 + (x[1] - 1)**2
    # fun = fun + np.random.uniform(-1, 1)

    # Himmelblau function
    fun = (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

    # Rastrigin function
    # fun = x[0]**2 + x[1]**2 - 10*(2 - np.cos( 2 * np.pi * x[0]) - np.cos( 2 * np.pi * x[1]))

    # Rosenbrock function
    # fun = 100*(x[1] - x[0]**2)**2 + (1 - x[0])**2

    # Ackley function
    # fun = -20 * np.exp( -0.2 * np.sqrt( 0.5 * (x[0]**2 + x[1]**2))) - \
    #     np.exp( 0.5 * (np.cos( 2 * np.pi * x[0]) + np.cos( 2 * np.pi * x[1]))) + np.e + 20

    return fun


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


def progress(iter_num, x):
    # Print current stage of optimization process
    print(f"Iteration  {iter_num:3d}   x = [{x[0]:9.5f},  {x[1]:9.5f}] of =  {func(x):9.5f}")
    return


eps = 1.e-4
x0 = np.array([0, 1])
path = [x0, ]
d1 = np.array([1, 0])
d2 = np.array([0, 1])
progress(0, x0)
for i in range(10):
    x1 = gs.gold_section_d(x0, d1, func, eps)
    path.append(x1)
    x2 = gs.gold_section_d(x1, d2, func, eps)
    path.append(x2)
    x3 = gs.gold_section_d(x2, d1, func, eps)
    path.append(x3)
    gradNew = x3 - x1
    xOpt = gs.gold_section_d(x3, gradNew, func, eps)
    progress(i + 1, xOpt)
    if np.linalg.norm(xOpt - x0, 2) < eps:
        break
    x0 = xOpt.copy()
    d1 = d2.copy()
    d2 = gradNew.copy()
