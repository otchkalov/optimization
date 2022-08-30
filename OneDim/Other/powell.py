# Powell quadratic approximation method

import numpy as np

def func(x):
    # fun = (x - 1)**2  # [0.0; 2.0]
    # fun = x**2 * (x**2 - 4) + 6   # [0.0; 2.0] then shift 0.0 to 0.5, 1.0
    fun = -np.cos(3*x)  # [1.5; 2.5]
    # fun = 2 * x**2 + 16.0 / x   # [0.5; 2.5]
    return fun


def order(x, f, numOpt):
    change = True
    xOrd = x
    fOrd = f

    number = [0, 1, 2, 3]
    while change:
        change = False
        for i in range(3):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                f[i], f[i+1] = f[i+1], f[i]
                number[i], number[i+1] = number[i+1], number[i]
                change = True
        
    for i in range(4):
        if number[i] == numOpt:
            numNew = i
            break
    return [x, f, numNew]


x = np.zeros(4)
f = np.zeros(4)
delta = 0.5
searchErr = 1.0e-4
x[0] = 1.5
x[1] = x[0] + delta
f[0] = func(x[0])
f[1] = func(x[1])
if f[0] > f[1]:
    x[2] = x[0] + 2 * delta
else:
    x[2] = x[0] - delta
f[2] = func(x[2])

xOpt = x[0]
fOpt = f[0]
print("  i           x_1           x_2         x_3           x_min        f_min")
print("------------------------------------------------------------------------")

for i in range(10):
    a0 = f[0]
    a1 = (f[1] - f[0])/(x[1] - x[0])
    a2 = (f[2] - f[1] - (f[1] - f[0])*(x[2] - x[0])/(x[1] - x[0]))/((x[2] - x[0])*(x[2] - x[1]))
    
    xQuad = (x[0] + x[1])/2 - a1/(2*a2)
    fQuad = func(xQuad)
    
    nMin = np.argmin(f)
    fMin = f[nMin]
    xMin = x[nMin]
    print(f"{i:3d}  {x[0]:12.5f}  {x[1]:12.5f}  {x[2]:12.5f}  {xMin:12.5f}  {fMin:12.5f}")
  
    if fQuad < fMin:
        nMin = 3
    
    x[3] = xQuad
    f[3] = fQuad
    
    [xOrd, fOrd, numNew] = order(x, f, nMin)
    
    # Choose new 3 points: optimal and 2 on both sides of it
    if numNew == 0:
        x[0] = xOrd[0] - delta
        f[0] = func(x[0])
        x[1] = xOrd[0]
        f[1] = fOrd[0]
        x[2] = xOrd[1]
        f[2] = fOrd[1]
    elif numNew == 3:
        x[0] = xOrd[2]
        f[0] = fOrd[2]
        x[1] = xOrd[3]
        f[1] = fOrd[3]
        x[2] = xOrd[3] + delta
        f[2] = func(x[3])
    else:
        x[0] = xOrd[numNew - 1]
        f[0] = fOrd[numNew - 1]
        x[1] = xOrd[numNew]
        f[1] = fOrd[numNew]
        x[2] = xOrd[numNew + 1]
        f[2] = fOrd[numNew + 1]

    q = a0 + a1 * (x[1] - x[0]) + a2 * (x[1] - x[0]) * (x[1] - x[3])
    if (np.abs(x[1] - xOpt) < searchErr) & (np.abs(f[1] - q) < searchErr):
        break
    
    xOpt = x[1]
    fOpt = f[1]

print(f"{i+1:3d}  {x[0]:12.5f}  {x[1]:12.5f}  {x[2]:12.5f}  {xMin:12.5f}  {fMin:12.5f}\n")
print(f"xOpt = {xOpt:12.5g}  fOpt = {fOpt:12.5g}  numIters = {i}")

if i >= 9:
    print("No convergation after 10 steps")
