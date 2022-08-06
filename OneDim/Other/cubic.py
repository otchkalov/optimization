# Use cubic approximation to estimate the OF minimum.

import numpy as np
import plotter

def ofdf(x):
    # fun = (x - 1)**2  # [0.0; 2.0]
    # fun = x**2 * (x**2 - 4) + 6   # [0.0; 2.0] then shift 0.0 to 0.5, 1.0
    # fun = -np.cos(3*x)  # [1.5; 2.5]
    fun = 2 * x**2 + 16.0 / x   # [0.5; 2.5]
    dfdx = 4 * x - 16.0 / x**2
    return [fun, dfdx]

x  = np.zeros(3)
f  = np.zeros(3)
df = np.zeros(3)
x[0] = 1.
x[1] = 2.

searchErr = 1.0e-4
plot_graph = True

f[0], df[0] = ofdf(x[0])
f[1], df[1] = ofdf(x[1])

xOpt = x[0]
fOpt = f[0]
print("  i           x_1           x_2         x_3           x_min        f_min")
print("------------------------------------------------------------------------")

for i in range(10):
    z = 3 * (f[0] - f[1]) / (x[1] - x[0]) + df[0] + df[1]
    w = np.sqrt( z**2 - df[0] * df[1])
    mu = (df[1] + w - z) / (df[1] - df[0] + 2 * w)
    x[2] = x[1] - mu * (x[1] - x[0])
    f[2], df[2] = ofdf(x[2])
    print(f"{i:3d}  {x[0]:12.5f}  {x[1]:12.5f}  {x[2]:12.5f}  {xOpt:12.5f}  {fOpt:12.5f}")
    if (np.abs( x[2] - xOpt ) < searchErr):
        break
    xOpt = x[2]
    fOpt = f[2]

    if plot_graph:
        #Generate points for objective function graph      
        arg = np.linspace(x[0], x[1], 100)
        y, dy = ofdf(arg)
        a0 = f[0]
        a1 = (f[1] - a0) / (x[1] - x[0])
        a2 = (df[0] - a1) / (x[0] - x[1])
        a3 = (df[1] - a1 - a2 * (x[1] - x[0])) / (x[1] - x[0]) ** 2
        approx = a0 + a1*(arg - x[0]) + a2*(arg - x[0]) * (arg - x[1]) + \
            a2*(arg - x[0])**2 * (arg - x[1])
        plotter.plot_graph(arg, y, approx, x[0], x[1])

    # Chooze a best couple of points
    if( f[0] < f[1]):
        x[1] = x[2]
        f[1] = f[2]
        df[1] = df[2]
    else:
        x[0] = x[2]
        f[0] = f[2]
        df[0] = df[2]
    

print("------------------------------------------------------------------------\n")
print(f"xOpt = {xOpt:12.5g}  fOpt = {fOpt:12.5g}  numIters = {i} ")
if i == 10:
    print("No convergation after 10 steps")
