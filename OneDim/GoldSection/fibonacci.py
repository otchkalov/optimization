import numpy as np

def func(x):
    fun = (x-1)**2
    return fun

# One-dim search using Fibonacci series

n = 12
fib = np.ones(n+3, dtype=np.float64)
for i in range(2, n+3): 
     fib[i] = fib[i-1] + fib[i-2];

xLeft = 0.0
xRight = 2.0
width = xRight - xLeft

x1 = xLeft + width*fib[n-3]/fib[n-1]
x2 = xLeft + width*fib[n-2]/fib[n-1]
f1 = func(x1)
f2 = func(x2)

print ("   xLeft      xRight     width      k2        k1")
print ("-------------------------------------------------------")

for i in range(n+2, 2, -1):
    if f1 < f2:
        xRight = x2
        width = xRight - xLeft
        x2 = x1
        f2 = f1
        x1 = xLeft + width*fib[i-3]/fib[i-1]
        f1 = func(x1)
    else:
        xLeft = x1
        width = xRight - xLeft
        x1 = x2
        f1 = f2
        x2 = xLeft + width*fib[i-2]/fib[i-1]
        f2 = func(x2)

    print (f" {xLeft:9.5f}  {xRight:9.5f}  {width:9.5f}  {fib[i-3]/fib[i-1]:9.5f} {fib[i-2]/fib[i-1]:9.5f} ")

xOpt = (x1 + x2) / 2
print("-------------------------------")
print(f"  xOpt = {xOpt:9.5f}")