# Svenn algorithm to search for interval of indefinite

# Input: starting point and initial step
def svenn(func, x0, step):
    x1 = x0 - step
    x2 = x0 + step
    f0 = func(x0)
    f1 = func(x1)
    f2 = func(x2)
    if (f1 > f0) & (f2 > f0):
        x_left = x1
        x_right = x2
        return x_left, x_right

    elif (f1 < f0) & (f2 < f0):
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
            # exclude worst interval
            if f1 > f3:
                x_left = x1
                x_right = x2
            else:
                x_left = x0
                x_right = x3
            if x_left > x_right:
                buf = x_left
                x_left, x_right = x_right, x_left
            print(f'DSK: found ({x_left:8.4f}, {x_right:8.4f}) interval in {i:2d} steps')
            return x_left, x_right

    print('Specified initial point is too far from minimum')
    return x0, x0
