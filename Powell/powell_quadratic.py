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
x0 = np.array([-1, 0])
d1 = np.array([1, 0])
d2 = np.array([0, 1])
path = [x0,]
x1 = gs.gold_section_d (x0, d1, func, EPS)
path.append(x1)
x2 = gs.gold_section_d (x1, d2, func, EPS)
path.append(x2)
x3 = gs.gold_section_d (x2, d1, func, EPS)
path.append(x3)
gradNew = x3 - x1
dirGrad = gradNew/np.linalg.norm(gradNew, 2)
path.append(x1)
xOpt = gs.gold_section_d (x3, dirGrad, func, EPS)
path.append(xOpt)
print(f"Optimal point: [{xOpt[0]:9.5f}, {xOpt[1]:9.5f}]")

# Objective function gradient plot
nPoints = 100
x1Lim = [-4, 4]
x2Lim = [-4, 4]
x1list = np.linspace(x1Lim[0], x1Lim[1], nPoints)
x2list = np.linspace(x2Lim[0], x2Lim[1], nPoints)
X1, X2 = np.meshgrid(x1list, x2list)
ObjFun = func([X1, X2])

plotter.plot_graph(X1, X2, ObjFun, path)
