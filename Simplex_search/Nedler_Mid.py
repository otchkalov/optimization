"""
Nedler-Mid modification of simplex search strategy
"""
import numpy as np
import plotter


def func(x):
    # Calculate object function value

    # Simple quadratic function
    of = (x[0] - 1) ** 2 + (x[1] - 1) ** 2 - x[0] * x[1]
    # of = (x[0] - 1)**2 + (x[1] - 1)**2
    # of = fun + np.random.uniform(-1, 1)

    # Himmelblau function
    # of = (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

    # Rastrigin function
    # of = x[0]**2 + x[1]**2 - 10*(2 - np.cos( 2 * np.pi * x[0]) - np.cos( 2 * np.pi * x[1]))

    # Rosenbrock function
    # of = 100*(x[1] - x[0]**2)**2 + (1 - x[0])**2

    # Ackley function
    # of = -20 * np.exp( -0.2 * np.sqrt( 0.5 * (x[0]**2 + x[1]**2))) - \
    #     np.exp( 0.5 * (np.cos( 2 * np.pi * x[0]) + np.cos( 2 * np.pi * x[1]))) + np.e + 20

    return of


def set_limits(func_name):
    switcher = {
        "quadratic": [[-4, 4], [-4, 4]],
        "Himmelblau": [[-5, 5], [-5, 5]],
        "Rasstrigin": [[-1, 1], [-1, 1]],
        "Rosenbrock": [[-2, 2], [-1, 3]],
        "Ackley": [[-4, 4], [-4, 4]]
    }
    limits = switcher.get(func_name, [[0, 0], [1, 1]])
    return limits[0], limits[1]


# Simplex search


def mirror(point, center, theta):
    return [point[0] + (1 + theta) * (center[0] - point[0]),
            point[1] + (1 + theta) * (center[1] - point[1])]


x0 = [-3, -3]  # Initial point
a = 0.5
EPS = 1.e-5
sq3 = np.sqrt(3)

# Build an initial simplex
simplex = [[x0[0],         x0[1] + a * sq3 / 3],
           [x0[0] + a / 2, x0[1] - a * sq3 / 6],
           [x0[0] - a / 2, x0[1] - a * sq3 / 6]]
fun = [func(simplex[0]), func(simplex[1]), func(simplex[2])]
# Collect simplexes for plot
simplex_set = [simplex.copy(), ]

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

    centralPoint = [(simplex[p1][0] + simplex[p2][0]) / 2, (simplex[p1][1] + simplex[p2][1]) / 2]
    newPoint = mirror(simplex[sMax], centralPoint, 1)
    newFun = func(newPoint)
    if newFun < fun[nOrder[2]]:
        simplex[sMax] = mirror(simplex[sMax], centralPoint, 2)
        fun[sMax] = func(simplex[sMax])
    elif newFun > fun[nOrder[0]]:
        simplex[sMax] = mirror(simplex[sMax], centralPoint, -0.5)
        fun[sMax] = func(simplex[sMax])
    elif newFun > fun[nOrder[1]]:
        simplex[sMax] = mirror(simplex[sMax], centralPoint, 0.5)
        fun[sMax] = func(simplex[sMax])
    else:
        simplex[sMax] = newPoint
        fun[sMax] = newFun

    simplex_set.append(simplex.copy())

    if max(fun) - min(fun) < EPS:
        break

# Objective function and minimization path plot
nPoints = 100
x1Lim, x2Lim = set_limits("quadratic")
x1list = np.linspace(x1Lim[0], x1Lim[1], nPoints)
x2list = np.linspace(x2Lim[0], x2Lim[1], nPoints)
X1, X2 = np.meshgrid(x1list, x2list)
ObjFun = func([X1, X2])

print(f"Optimal point [{simplex[0][0]:9.5f}, {simplex[0][1]:9.5f}]")

plotter.plot_graph(X1, X2, ObjFun, simplex_set)
