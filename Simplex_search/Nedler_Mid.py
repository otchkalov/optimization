"""
Nedler-Mid modification of simplex search strategy
"""
import numpy as np
import plotter
import of


def mirror(point, center, theta):
    return [
        point[0] + (1 + theta) * (center[0] - point[0]),
        point[1] + (1 + theta) * (center[1] - point[1]),
    ]


ofname = "quadratic"
x0 = [-3, -3]  # Initial point
a = 0.5
EPS = 1.0e-5
sq3 = np.sqrt(3)

# Build an initial simplex
simplex = [
    [x0[0], x0[1] + a * sq3 / 3],
    [x0[0] + a / 2, x0[1] - a * sq3 / 6],
    [x0[0] - a / 2, x0[1] - a * sq3 / 6],
]
fun = [
    of.func(simplex[0], ofname),
    of.func(simplex[1], ofname),
    of.func(simplex[2], ofname),
]
# Collect simplexes for plot
simplex_set = [
    simplex.copy(),
]

nOrder = [0, 1, 2]
for step in range(100):
    # Define an order of simplex nodes
    CHANGE = True
    while CHANGE:
        CHANGE = False
        for j in [0, 1]:
            if fun[nOrder[j]] < fun[nOrder[j + 1]]:
                nOrder[j], nOrder[j + 1] = nOrder[j + 1], nOrder[j]
                CHANGE = True

    # Mirror the worst point
    sMax = nOrder[0]
    p1 = nOrder[1]
    p2 = nOrder[2]

    centralPoint = [
        (simplex[p1][0] + simplex[p2][0]) / 2,
        (simplex[p1][1] + simplex[p2][1]) / 2,
    ]
    newPoint = mirror(simplex[sMax], centralPoint, 1)
    newFun = of.func(newPoint, ofname)
    if newFun < fun[nOrder[2]]:
        simplex[sMax] = mirror(simplex[sMax], centralPoint, 2)
        fun[sMax] = of.func(simplex[sMax], ofname)
    elif newFun > fun[nOrder[0]]:
        simplex[sMax] = mirror(simplex[sMax], centralPoint, -0.5)
        fun[sMax] = of.func(simplex[sMax], ofname)
    elif newFun > fun[nOrder[1]]:
        simplex[sMax] = mirror(simplex[sMax], centralPoint, 0.5)
        fun[sMax] = of.func(simplex[sMax], ofname)
    else:
        simplex[sMax] = newPoint
        fun[sMax] = newFun

    simplex_set.append(simplex.copy())

    if max(fun) - min(fun) < EPS:
        break

# Objective of.function and minimization path plot
nPoints = 100
x1Lim, x2Lim = of.set_limits(ofname)
x1list = np.linspace(x1Lim[0], x1Lim[1], nPoints)
x2list = np.linspace(x2Lim[0], x2Lim[1], nPoints)
X1, X2 = np.meshgrid(x1list, x2list)
ObjFun = of.func([X1, X2], ofname)

print(f"Optimal point [{simplex[0][0]:9.5f}, {simplex[0][1]:9.5f}]")

plotter.plot_graph(X1, X2, ObjFun, simplex_set)
