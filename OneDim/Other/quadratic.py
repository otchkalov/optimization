# Use quadratic approximation to estimate the OF minimum.

import numpy as np
import plotter

def func(x):
    # fun = (x - 1)**2  # [0.0; 2.0]
    # fun = x**2 * (x**2 - 4) + 6   # [0.0; 2.0] then shift 0.0 to 0.5, 1.0
    # fun = -np.cos(3*x)  # [1.5; 2.5]
    fun = 2 * x**2 + 16.0 / x   # [0.5; 2.5]
    return fun

plot_graph = True

xLeft = 0.5
xRight = 2.5
xMid = (xLeft + xRight)/2

f1 = func(xLeft)
f2 = func(xRight)
f3 = func(xMid)

a0 = f1
a1 = (f2 - f1)/(xRight - xLeft)
a2 = (f3 - f1 - (f2 - f1)*(xMid - xLeft)/(xRight - xLeft))/((xMid - xLeft)*(xMid - xRight))

if plot_graph:
    #Generate points for objective function graph      
    x = np.linspace(xLeft, xRight, 100)
    y = func(x)
    approx = a0 + a1*(x - xLeft) + a2*(x - xLeft) * (x - xRight)
    plotter.plot_graph(x, y, approx, xLeft, xRight)

xOpt = (xLeft + xRight)/2 - a1/(2*a2)
fOpt = func(xOpt)

print(f" xOpt = {xOpt:12.5g} fOpt = {fOpt:12.5g} \n")
