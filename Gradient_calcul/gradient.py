import numpy as np
import plotter


def func(x):
    # Calculate object function value

    # Simple quadratic function
    fun = (x[0] - 1) ** 2 + (x[1] - 1) ** 2 - x[0] * x[1]
    # fun = fun + np.random.uniform(-0.1, 0.1)
    x1Lim = [-4, 4]
    x2Lim = [-4, 4]
    levels = [-1.9, 0, 8, 16, 24, 32, 40, 48, 56]

    # Himmelblau function
    # fun = (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2
    # x1Lim = [-5, 5]
    # x2Lim = [-5, 5]
    # levels = [1.0, 16, 32, 48, 96, 200]

    # Rastrigin function
    # fun = x[0]**2 + x[1]**2 - 10*(2 - np.cos( 2 * np.pi * x[0]) - np.cos( 2 * np.pi * x[1]))
    # x1Lim = [-5, 5]
    # x2Lim = [-5, 5]
    # levels = [0.01, 0.5, 10., 20., 30., 40]

    # Rosenbrock function
    # fun = 100*(x[1] - x[0]**2)**2 + (1 - x[0])**2
    # x1Lim = [-2, 2]
    # x2Lim = [-1, 3]
    # levels = [1.0, 16, 32, 48, 96, 200]

    # Ackley function
    # fun = -20 * np.exp( -0.2 * np.sqrt( 0.5 * (x[0]**2 + x[1]**2))) - \
    #     np.exp( 0.5 * (np.cos( 2 * np.pi * x[0]) + np.cos( 2 * np.pi * x[1]))) + np.e + 20
    # x1Lim = [-4, 4]
    # x2Lim = [-4, 4]
    # levels = [1.0, 2, 4, 8, 16, 32]

    return fun, x1Lim, x2Lim, levels


def agradient(x):
    # Calculate object function antigradient

    h = 1.e-1
    grad = [0, 0]
    double_h = 2 * h

    grad[0] = -(func([x[0] + h, x[1]])[0] - func([x[0] - h, x[1]])[0]) / double_h
    grad[1] = -(func([x[0], x[1] + h])[0] - func([x[0], x[1] - h])[0]) / double_h

    return grad


# Objective function gradient plot
nPoints = 20
ObjFun, x1Lim, x2Lim, levels = func([0, 0])  # Just to get limits
x1list = np.linspace(x1Lim[0], x1Lim[1], nPoints)
x2list = np.linspace(x2Lim[0], x2Lim[1], nPoints)
X1, X2 = np.meshgrid(x1list, x2list)
ObjFun, x1Lim, x2Lim, levels = func([X1, X2])
gradOf = agradient([X1, X2])

# plotter.plot_graph(X1, X2, ObjFun, levels)
plotter.vector_plot(X1, X2, ObjFun, gradOf, levels)
