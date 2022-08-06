# Svenn algorithm to search for interval of inderinite

# Input: starting point and initial step
def svenn(func, x0, step):
    x1 = x0 - step
    x2 = x0 + step
    f0 = func(x0)
    f1 = func(x1)
    f2 = func(x2)
    if (f1 > f0) & (f2 > f0):
        xLeft = x1
        xRight = x2
        return xLeft, xRight

    elif (f1<f0) & (f2 < f0):
        print('Incorrect initial value. Function is not unimodal on the interval')
        return x0, x0
    
    if f1 <= f2:
        step = -step
    else:
        x1 = x2
        f1 = f2

    for i in range(10):
        step *= 2
        x2 = x1 + step
        f2 = func(x2)
        if f2 <= f1:
            # continue search
            x0 = x1
            x1 = x2
            f1 = f2
        else:
            # make half-step back
            x3 = x2 - step/2
            f3 = func(x3)
            # exclude wrost interval
            if f1 > f3:
                xLeft = x1
                xRight = x2
            else:
                xLeft = x0
                xRight = x3
            if xLeft > xRight:
                buf = xLeft
                xLeft = xRight
                xRight = buf
            return xLeft, xRight

    print('Specified initial point is too far from minimum')
    return x0, x0
