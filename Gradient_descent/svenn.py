# Svenn algorithm to search for interval of inderinite
# in direction of coordNum coordinate for 2-variable function

# Input: starting point, coordinate number, object functuion procedure and initial step
def svenn(x0, coordNum, func, step):
    x1 = x0.copy()
    x1[coordNum] = x0[coordNum] - step
    x2 = x0.copy()
    x2[coordNum] = x0[coordNum] + step
    f0 = func(x0)
    f1 = func(x1)
    f2 = func(x2)
    if (f1 > f0) & (f2 > f0):
        xLeft = x1.copy()
        xRight = x2.copy()
        return xLeft, xRight

    elif (f1<f0) & (f2 < f0):
        print('Incorrect initial value. Function is not unimodal on the interval')
        return x0, x0
    
    if f1 <= f2:
        step = -step
    else:
        x1 = x2.copy()
        f1 = f2

    for i in range(10):
        step *= 2
        x2 = x1.copy()
        x2[coordNum] = x1[coordNum] + step
        f2 = func(x2)
        if f2 <= f1:
            # continue search
            x0 = x1.copy()
            x1 = x2.copy()
            f1 = f2
        else:
            # make half-step back
            x3 = x2.copy()
            x3[coordNum] = x2[coordNum] - step/2
            f3 = func(x3)
            # exclude wrost interval
            if f1 > f3:
                xLeft = x1.copy()
                xRight = x2.copy()
            else:
                xLeft = x0.copy()
                xRight = x3.copy()
            if xLeft[coordNum] > xRight[coordNum]:
                xLeft, xRight = xRight.copy(), xLeft.copy()
            return xLeft, xRight

    print('Specified initial point is too far from minimum')
    return x0, x0
