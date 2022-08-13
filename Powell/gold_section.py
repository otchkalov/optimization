# Gold section search in given direction
# Input: starting point, direction orth, object functuion procedure and accuracy
def gold_section_d(x0, dirVec, func, eps = 1.e-5):

    # Apply Svenn algorithm for interval search
    step = 0.1
    xLeft, xRight = svenn_d(x0, dirVec, func, step)

    # Start "gold section" process
    # Scalar product of (xRight - xLeft) on dirVec of length 1 results interval length
    length = (xRight[0] - xLeft[0])*dirVec[0] + (xRight[1] - xLeft[1])*dirVec[1]
    x1 = [xLeft[0] + 0.382*length*dirVec[0], xLeft[1] + 0.382*length*dirVec[1] ]
    x2 = [xLeft[0] + 0.618*length*dirVec[0], xLeft[1] + 0.618*length*dirVec[1] ]
    f1 = func(x1)
    f2 = func(x2)

    for i in range(100):
        if (f1 < f2):
            # exclude right interval
            xRight = x2.copy()
            length = (xRight[0] - xLeft[0])*dirVec[0] + (xRight[1] - xLeft[1])*dirVec[1]
            x2 = x1.copy()
            f2 = f1
            x1 = [xLeft[0] + 0.382*length*dirVec[0], xLeft[1] + 0.382*length*dirVec[1] ]
            f1 = func(x1)
        else:
            # exclude left interval
            xLeft = x1.copy()
            length = (xRight[0] - xLeft[0])*dirVec[0] + (xRight[1] - xLeft[1])*dirVec[1]
            x1 = x2.copy()
            f1 = f2
            x2 = xLeft.copy()
            x2 = [xLeft[0] + 0.618*length*dirVec[0], xLeft[1] + 0.618*length*dirVec[1] ]
            f2 = func(x2)
        if length < eps:
           break
    if (i == 99):
        print('Warning: Required accuracy cannot be reached in 100 steps')
    # Return left margin as an optimal point
    return xLeft 

# Svenn algorithm to search for interval of indefinity
# in given direction for 2-variable function

# Input: starting point, direction vector, object functuion procedure and initial step
def svenn_d(x0, dirVec, func, step):
    x1 = [ x0[0] - step*dirVec[0], x0[1] - step*dirVec[1] ]
    x2 = [ x0[0] + step*dirVec[0], x0[1] + step*dirVec[1] ]
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
        x2 = [ x1[0] + step*dirVec[0], x1[1] + step*dirVec[1] ]
        f2 = func(x2)
        if f2 <= f1:
            # continue search
            x0 = x1.copy()
            x1 = x2.copy()
            f1 = f2
        else:
            # make half-step back
            x3 = [ x2[0] + 0.5*step*dirVec[0], x2[1] + 0.5*step*dirVec[1] ]
            f3 = func(x3)
            # exclude wrost interval
            if f1 > f3:
                xLeft = x1.copy()
                xRight = x2.copy()
            else:
                xLeft = x0.copy()
                xRight = x3.copy()
            if (xRight[0] - xLeft[0])*dirVec[0] + (xRight[1] - xLeft[1])*dirVec[1] < 0:
                xLeft, xRight = xRight.copy(), xLeft.copy()
            return xLeft, xRight

    print('Specified initial point is too far from minimum')
    return x0, x0
