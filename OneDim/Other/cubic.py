# Use cubic approximation to estimate the OF minimum.

import numpy as np
import plotter


def ofdf(arg):
    # fun = (arg - 1) ** 2  # [0.0; 2.0]
    # dfdx = 2 * (arg - 1)
    fun = arg ** 2 * (arg ** 2 - 4) + 6   # [0.0; 2.0] then shift 0.0 to 0.5, 1.0
    dfdx = 4 * arg ** 3 - 8 * arg
    # fun = -np.cos(arg)  # [1.5; 2.5]
    # dfdx = np.sin(arg)
    # fun = 2 * arg ** 2 + 16.0 / arg  # [0.5; 2.5]
    # dfdx = 4 * arg - 16.0 / arg ** 2
    return [fun, dfdx]


# Node points, fun values and derivative values
x_n = np.zeros(3)
f_n = np.zeros(3)
df_n = np.zeros(3)
x_n[0] = 0.
x_n[1] = 2.0

searchErr = 1.0e-4
plot_graph = True

f_n[0], df_n[0] = ofdf(x_n[0])
f_n[1], df_n[1] = ofdf(x_n[1])

xOpt = x_n[0]
fOpt = f_n[0]
print("  i           x_1           x_2         x_3           x_min        f_min")
print("------------------------------------------------------------------------")

for i in range(10):
    z = 3 * (f_n[0] - f_n[1]) / (x_n[1] - x_n[0]) + df_n[0] + df_n[1]
    w = np.sqrt(z ** 2 - df_n[0] * df_n[1])
    mu = (df_n[1] + w - z) / (df_n[1] - df_n[0] + 2 * w)
    x_n[2] = x_n[1] - mu * (x_n[1] - x_n[0])
    f_n[2], df_n[2] = ofdf(x_n[2])

    if plot_graph:
        # Generate points for objective function graph
        x = np.linspace(x_n[0], x_n[1], 100)
        y, dy = ofdf(x)
        a0 = f_n[0]
        a1 = (f_n[1] - a0) / (x_n[1] - x_n[0])
        a2 = (df_n[0] - a1) / (x_n[0] - x_n[1])
        a3 = (df_n[1] - a1 - a2 * (x_n[1] - x_n[0])) / (x_n[1] - x_n[0]) ** 2
        approx = a0 + a1 * (x - x_n[0]) + a2 * (x - x_n[0]) * (x - x_n[1]) + \
                 a3 * (x - x_n[0]) ** 2 * (x - x_n[1])
        plotter.plot_graph(x, y, approx, x_n[0], x_n[1])

    xOpt_prev = xOpt
    xOpt = x_n[2]
    fOpt = f_n[2]
    print(f"{i:3d}  {x_n[0]:12.5f}  {x_n[1]:12.5f}  {x_n[2]:12.5f}  {xOpt:12.5f}  {fOpt:12.5f}")
    # Can we complete the search?
    if np.abs(xOpt_prev - xOpt) < searchErr:
        break
    xOpt_prev = xOpt

    # Choose the best couple of points
    if f_n[0] < f_n[1]:
        x_n[1] = x_n[2]
        f_n[1] = f_n[2]
        df_n[1] = df_n[2]
    else:
        x_n[0] = x_n[2]
        f_n[0] = f_n[2]
        df_n[0] = df_n[2]

print("------------------------------------------------------------------------\n")
print(f"xOpt = {xOpt:12.5g}  fOpt = {fOpt:12.5g}  numIters = {i} ")
if i == 10:
    print("No convergence after 10 steps")
