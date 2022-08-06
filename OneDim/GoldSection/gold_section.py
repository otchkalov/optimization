import numpy as np
import time
import plotter
import svenn


def func(x):
    fun = (x-1)**2
    return fun


svenn_int = False
plot_graph = False


if svenn_int:
    # Apply Svenn algorithm for interval search
    x0 = 0.5
    step = 0.1
    xLeft, xRight = svenn.svenn(func, x0, step)
else:
    # Set interval limits manually
    xLeft  = 0.5
    xRight = 2.0
    
if xLeft == xRight:
    exit()

eps = 1.e-2

if plot_graph:
    #Generate point for objective function graph      
    x = np.linspace(xLeft, xRight, 100)
    y = func(x)

print(f'xLeft = {xLeft:12.5f}    xRight = {xRight:12.5f}  length = {xRight - xLeft:12.5f} \n')

print('  i           x_1           x_2         f_1           f_2        length')
print('------------------------------------------------------------------------')


# Start "gold section" process
length = xRight - xLeft
x1 = xLeft + 0.382*length
x2 = xLeft + 0.618*length
f1 = func(x1)
f2 = func(x2)
print(f'{0:3d}  {x1:12.5f}  {x2:12.5f}  {f1:12.5f}  {f2:12.5f}  {length:12.5f}')
if plot_graph:
    plotter.plot_graph(x, y, func, xLeft, xRight, x1, x2)
    time.sleep(1)

for i in range(20):
    if (f1 < f2):
        # exclude right interval
        xRight = x2
        length = xRight - xLeft
        x2 = x1
        f2 = f1
        x1 = xLeft + 0.382*length
        f1 = func(x1)
    else:
        # exclude left interval
        xLeft = x1
        length = xRight - xLeft
        x1 = x2
        f1 = f2
        x2 = xLeft + 0.618*length
        f2 = func(x2)

    print(f'{i:3d}  {x1:12.5f}  {x2:12.5f}  {f1:12.5f}  {f2:12.5f}  {length:12.5f}')
    if plot_graph:
        plotter.plot_graph(x, y, func, xLeft, xRight, x1, x2)
        time.sleep(1)
    if length < eps:
        break

if (i == 19):
    print('Warning: Required accuracy cannot be reached in 20 steps')
