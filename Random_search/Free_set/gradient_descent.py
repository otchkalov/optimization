import numpy as np
import plotter
import gold_section as gs

def  func(x):
# Calculate object function value

    # Simple quadratic function
    # x1Lim = [-4, 4]
    # x2Lim = [-4, 4]
    fun = (x[0] - 1)**2 + (x[1] - 1)**2 - x[0]*x[1]
    # fun = (x[0] - 1)**2 + (x[1] - 1)**2
    # fun = fun + np.random.uniform(-1, 1)

    # Himmelblau function
    # x1Lim = [-5, 5]
    # x2Lim = [-5, 5]
    # fun = (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

    # Rastrigin function
    # x1Lim = [-1, 1]
    # x2Lim = [-1, 1]
    # fun = x[0]**2 + x[1]**2 - 10*(2 - np.cos( 2 * np.pi * x[0]) - np.cos( 2 * np.pi * x[1]))

    # Rosenbrock function
    # x1Lim = [-2, 2]
    # x2Lim = [-1, 3]
    # fun = 100*(x[1] - x[0]**2)**2 + (1 - x[0])**2

    # Ackley function
    # x1Lim = [-4, 4]
    # x2Lim = [-4, 4]
    # fun = -20 * np.exp( -0.2 * np.sqrt( 0.5 * (x[0]**2 + x[1]**2))) - \
    #     np.exp( 0.5 * (np.cos( 2 * np.pi * x[0]) + np.cos( 2 * np.pi * x[1]))) + np.e + 20

    return fun

def agradient(x):
    # Calculate object function antigradient

    h = 1.e-1
    grad = [0, 0]
    doubleH = 2*h

    grad[0] = -(func( [x[0] + h, x[1]]) - func( [x[0] - h, x[1]])) / doubleH
    grad[1] = -(func( [x[0], x[1] + h]) - func( [x[0], x[1] - h])) / doubleH

    return grad


# Simple gradient descent
x_0 = [-1, -3]
eps = 1.e-3
path = [x_0,]
step = 0.1
print(f"{0:4d}  x_1 = {x_0[0]:12.5g}  x_2 = {x_0[1]:12.5g}")
for i in range(100):
    agrad = agradient(x_0)
    x_1 = [x_0[0] + step*agrad[0], x_0[1] + step*agrad[1]]
    print(f"{i+1:4d}  x_1 = {x_1[0]:12.5g}  x_2 = {x_1[1]:12.5g}")
    path.append(x_1)
    if step*np.linalg.norm(agrad,2) < eps:
        x_opt = x_1
        break
    else:
        x_0 = x_1

# Objective function and minimization path plot
nPoints = 100
x1Lim = [-4, 4]
x2Lim = [-4, 4]
x1list = np.linspace(x1Lim[0], x1Lim[1], nPoints)
x2list = np.linspace(x2Lim[0], x2Lim[1], nPoints)
X1, X2 = np.meshgrid(x1list, x2list)
ObjFun = func([X1, X2])

plotter.plot_graph(X1, X2, ObjFun, path)
