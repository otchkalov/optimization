import numpy as np
import time
import plotter
import svenn


def func(arg):
    global numOfCalc
    fun = (arg - 1) ** 2
    numOfCalc = numOfCalc + 1
    return fun


svenn_int = True
plot_graph = True

eps = 1.e-5
maxIter = 20
numOfCalc = 0

if svenn_int:
    # Apply Svenn algorithm for interval search
    x0 = 0.5
    step = 0.01
    xLeft, xRight = svenn.svenn(func, x0, step)
    print(f'Number of OF calculations for DSK {numOfCalc:3d}')
    numOfCalc = 0
else:
    # Set interval limits manually
    xLeft = 0.5
    xRight = 2.0
    
if xLeft == xRight:
    exit()

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
    # Generate point for objective function graph
    x = np.linspace(xLeft, xRight, 100)
    y = func(x)
    plotter.plot_graph(x, y, func, xLeft, xRight, x1, x2)
    time.sleep(1)

for i in range(maxIter):
    if f1 < f2:
        # exclude right interval
        xRight = x2
        length = xRight - xLeft
        x2 = x1
        f2 = f1
        x1 = xLeft + 0.382*length
        f1 = func(x1)
    elif f1 > f2:
        # exclude left interval
        xLeft = x1
        length = xRight - xLeft
        x1 = x2
        f1 = f2
        x2 = xLeft + 0.618*length
        f2 = func(x2)
    else:
        # exclude left and right intervals
        xLeft = x1
        xRight = x2
        length = xRight - xLeft
        x1 = xLeft + 0.382*length    
        x2 = xLeft + 0.618*length
        f1 = func(x1)
        f2 = func(x2)

    print(f'{i+1:3d}  {x1:12.5f}  {x2:12.5f}  {f1:12.5f}  {f2:12.5f}  {length:12.5f}')
    if plot_graph:
        plotter.plot_graph(x, y, func, xLeft, xRight, x1, x2)
        time.sleep(1)
    if length < eps:
        break
    if i == maxIter - 1:
        print(f'Warning: Required accuracy cannot be reached in {maxIter} steps')
    
print("\n ---------------------------------------------------------------------------------------\n")
print(f"xOpt = {x1:9.5f}   Number of OF calculations for gold section: {numOfCalc}")
