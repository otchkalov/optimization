# Uniform regular search

import numpy as np
import plotter

def func(x):
    # fun = (x - 1)**2  # [0.0; 2.0]
    fun = x**2 * (x**2 - 4) + 6   # [0.0; 2.0] then shift 0.0 to 0.5, 1.0
    # fun = -np.cos(3*x)  # [1.5; 2.5]
    # fun = 2 * x**2 + 16.0 / x   # [0.5; 2.5]
    return fun

xLeft  = 0.0
xRight = 2.0
width = xRight - xLeft
searchErr = 0.01
INF = 1.e8

numPoints = np.int32(width/searchErr + 1)
x = np.linspace(xLeft, xRight, numPoints)
f = np.zeros(numPoints, dtype=np.float64)

xOpt = x[0]
fOpt = INF

for k in range(numPoints):
    f[k] = func(x[k])
    if f[k] < fOpt: 
        xOpt = x[k]
        fOpt = f[k]

print(f"xOpt = {xOpt:12.5g}  fOpt = {fOpt:12.5g}  numPoints = {numPoints:5d} ")
plotter.plot_graph(x, f, f, xLeft, xRight)
