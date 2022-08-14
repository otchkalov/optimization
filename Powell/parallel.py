"""
Powell method for quadratic function
"""
import numpy as np
import gold_section as gs
import plotter


def func(x):
    # Calculate object function value
    of = (x[0] - 1) ** 2 + (x[1] - 1) ** 2 - x[0] * x[1]
    # of = (x[0] - 1)**2 + (x[1] - 1)**2
    # of = fun + np.random.uniform(-1, 1)
    return of


EPS = 1.e-3
a1 = np.array([0, 1])
a2 = np.array([0, 0])
grad = np.array([1, 0])
m1 = gs.gold_section_d(a1, grad, func, EPS)
m2 = gs.gold_section_d(a2, grad, func, EPS)
dirNew = (m2 - m1) / np.linalg.norm(m2 - m1, 2)
xOpt = gs.gold_section_d(m1, dirNew, func, EPS);

print(f"Optimal point: [{xOpt[0]:9.5f}, {xOpt[1]:9.5f}]")

# Objective function gradient plot
path = [a1, m1, m2, a2, m2, xOpt]
nPoints = 100
x1Lim = [-4, 4]
x2Lim = [-4, 4]
x1list = np.linspace(x1Lim[0], x1Lim[1], nPoints)
x2list = np.linspace(x2Lim[0], x2Lim[1], nPoints)
X1, X2 = np.meshgrid(x1list, x2list)
ObjFun = func([X1, X2])

plotter.plot_graph(X1, X2, ObjFun, path)
