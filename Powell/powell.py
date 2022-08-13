"""
Powell method for arbitrary function
"""
import numpy as np
import gold_section as gs
import plotter
import numpy as np


def  func(x):
# Calculate object function value

    # Simple quadratic function
    # fun = (x[0] - 1)**2 + (x[1] - 1)**2 - x[0]*x[1]
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


EPS = 1.e-4;
x0 = np.array([0, 1])
d1 = np.array([1, 0])
d2 = np.array([0, 1])
path = [x0,]
for i in range(10):
    x1 = gs.gold_section_d (x0, d1, func, EPS)
    path.append(x1)
    x2 = gs.gold_section_d (x1, d2, func, EPS)
    path.append(x2)
    x3 = gs.gold_section_d (x2, d1, func, EPS)
    path.append(x3)
    dirNew = (x3 - x1)/np.linalg.norm(x3 - x1, 2)
    xOpt = gs.gold_section_d (x3, dirNew, func, EPS)
    path.append(x1)
    path.append(xOpt)
    if np.linalg.norm(xOpt - x1, 2) < EPS:
        break
    x0 = xOpt.copy()
    d1 = d2.copy()
    d2 = dirNew.copy()

print(f"Optimal point: [{xOpt[0]:9.5f}, {xOpt[1]:9.5f}]")

# Objective function gradient plot
nPoints = 100
x1Lim, x2Lim = set_limits("Himmelblau")
x1list = np.linspace(x1Lim[0], x1Lim[1], nPoints)
x2list = np.linspace(x2Lim[0], x2Lim[1], nPoints)
X1, X2 = np.meshgrid(x1list, x2list)
ObjFun = func([X1, X2])

plotter.plot_graph(X1, X2, ObjFun, path)
