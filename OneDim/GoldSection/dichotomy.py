import numpy as np
import plotter
import time


def func(x):
    fun = (x-1)**2
    return fun


plot_graph = False

xLeft  = 0.5
xRight = 2.0

eps = 1.e-5

if plot_graph:
    #Generate point for objective function graph      
    x = np.linspace(xLeft, xRight, 100)
    y = func(x)

print(f'xLeft = {xLeft:8.5f}    xRight = {xRight:8.5f}  length = {xRight - xLeft:8.5f} \n')

print('  i           x_1           x_m           x_2         f_1         f_m           f_2        length')
print('---------------------------------------------------------------------------------------------------')


# Start dochotomy process
length = xRight - xLeft
x1 = xLeft + 0.25*length
x2 = xLeft + 0.75*length
xm = xLeft + 0.50*length
f1 = func(x1)
f2 = func(x2)
fm = func(xm)
print(f'{0:3d}  {x1:12.5f}  {xm:12.5f}  {x2:12.5f}  {f1:12.5f}  {fm:12.5f}  {f2:12.5f}  {length:12.5f}')
if plot_graph:
    plotter.plot_graph3(x, y, func, xLeft, xRight, x1, x2, xm)
    time.sleep(1)

for i in range(20):
    if (f1 < fm) & (fm < f2):
        # exclude right half of interval
        xRight = xm
        xm = x1
        fm = f1
    elif (f2 < fm) & (fm < f1):
        # exclude left half of interval
        xLeft = xm
        xm = x2
        fm = f2
    else:
        # exclude 2 peripherial quarters
        xLeft = x1
        xRight = x2
    # Note: we never have to recalculate OF value for new xm
    length = xRight - xLeft
    x1 = xLeft + 0.25*length
    x2 = xLeft + 0.75*length
    f1 = func(x1)
    f2 = func(x2)
        

    print(f'{i:3d}  {x1:12.5f}  {xm:12.5f}  {x2:12.5f}  {f1:12.5f}  {fm:12.5f}  {f2:12.5f}  {length:12.5f}')
    if plot_graph:
        plotter.plot_graph3(x, y, func, xLeft, xRight, x1, x2, xm)
        time.sleep(1)
    if length < eps:
        break

if (i == 19):
    print('Warning: Required accuracy cannot be reached in 20 steps')
