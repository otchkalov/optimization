"""
First realization of simplex search strategy
"""
import numpy as np
import plotter
import of

# Simplex search
ofname = "quadratic"
x0 = [-3, -3]  # initial point
a = 0.5
EPS = 1.0e-1
sq3 = np.sqrt(3)
mu = 0.5

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

nStab = [0, 0, 0]
sMax = 0
nOrder = [0, 1, 2]
sPrev = 0

for iter in range(100):
    # Define an order of simplex nodes
    CHANGE = True
    while CHANGE:
        CHANGE = False
        for j in [0, 1]:
            if fun[nOrder[j]] < fun[nOrder[j + 1]]:
                nOrder[j], nOrder[j + 1] = nOrder[j + 1], nOrder[j]
                CHANGE = True

    # Mirror the wrost point
    sMax = nOrder[0]
    p1 = nOrder[1]
    p2 = nOrder[2]

    if sMax == sPrev:
        # If the same vertex should be mirrored once again, choose the next vertex instead
        nOrder[1], nOrder[0] = nOrder[0], nOrder[1]
        p1 = nOrder[1]
        sMax = nOrder[0]

    nStab[sMax] = 0
    nStab[p1] = nStab[p1] + 1
    nStab[p2] = nStab[p2] + 1
    centralPoint = [
        (simplex[p1][0] + simplex[p2][0]) / 2,
        (simplex[p1][1] + simplex[p2][1]) / 2,
    ]
    simplex[sMax] = [
        2 * centralPoint[0] - simplex[sMax][0],
        2 * centralPoint[1] - simplex[sMax][1],
    ]
    fun[sMax] = of.func(simplex[sMax], ofname)
    sPrev = sMax

    simplex_set.append(simplex.copy())

    # Scale simplex if necessary
    if nStab[0] > 3:
        simplex[1] = [
            simplex[0][0] + mu * (simplex[1][0] - simplex[0][0]),
            simplex[0][1] + mu * (simplex[1][1] - simplex[0][1]),
        ]
        simplex[2] = [
            simplex[0][0] + mu * (simplex[2][0] - simplex[0][0]),
            simplex[0][1] + mu * (simplex[2][1] - simplex[0][1]),
        ]
        nStab = [0, 0, 0]
        a = mu * a
    elif nStab[1] > 3:
        simplex[2] = [
            simplex[1][0] + mu * (simplex[2][0] - simplex[1][0]),
            simplex[1][1] + mu * (simplex[2][1] - simplex[1][1]),
        ]
        simplex[0] = [
            simplex[1][0] + mu * (simplex[2][0] - simplex[0][0]),
            simplex[1][1] + mu * (simplex[0][1] - simplex[1][1]),
        ]
        nStab = [0, 0, 0]
        a = mu * a
    elif nStab[2] > 3:
        simplex[0] = [
            simplex[2][0] + mu * (simplex[0][0] - simplex[2][0]),
            simplex[2][1] + mu * (simplex[0][1] - simplex[2][1]),
        ]
        simplex[1] = [
            simplex[2][0] + mu * (simplex[1][0] - simplex[2][0]),
            simplex[2][1] + mu * (simplex[1][1] - simplex[2][1]),
        ]
        nStab = [0, 0, 0]
        a = mu * a
    # Finalization criteria
    if a < EPS:
        break


# Objective function and minimization path plot
nPoints = 100
x1Lim, x2Lim = of.set_limits(ofname)
x1list = np.linspace(x1Lim[0], x1Lim[1], nPoints)
x2list = np.linspace(x2Lim[0], x2Lim[1], nPoints)
X1, X2 = np.meshgrid(x1list, x2list)
ObjFun = of.func([X1, X2], ofname)

print(f"Optimal point [{simplex[0][0]:9.5f}, {simplex[0][1]:9.5f}]")

plotter.plot_graph(X1, X2, ObjFun, simplex_set)
