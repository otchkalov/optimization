# Gold section algorithm to search for a local minimum
# in direction of coordNum coordinate for 2-variable function

import svenn

# Input: starting point, coordinate number, object functuion procedure and accuracy
def gold_section(x0, coordNum, func, eps = 1.e-5):

    # Apply Svenn algorithm for interval search
    step = 0.1
    xLeft, xRight = svenn.svenn(x0, coordNum, func, step)

    # Start "gold section" process
    length = xRight[coordNum] - xLeft[coordNum]
    x1 = xLeft.copy()
    x1[coordNum] = xLeft[coordNum] + 0.382*length
    x2 = xLeft.copy()
    x2[coordNum] = xLeft[coordNum] + 0.618*length
    f1 = func(x1)
    f2 = func(x2)

    for i in range(100):
        if (f1 < f2):
            # exclude right interval
            xRight = x2.copy()
            length = xRight[coordNum] - xLeft[coordNum]
            x2 = x1.copy()
            f2 = f1
            x1 = xLeft.copy()
            x1[coordNum] = xLeft[coordNum] + 0.382*length
            f1 = func(x1)
        else:
            # exclude left interval
            xLeft = x1.copy()
            length = xRight[coordNum] - xLeft[coordNum]
            x1 = x2.copy()
            f1 = f2
            x2 = xLeft.copy()
            x2[coordNum] = xLeft[coordNum] + 0.618*length
            f2 = func(x2)
        if length < eps:
           break
    if (i == 99):
        print('Warning: Required accuracy cannot be reached in 100 steps')
    # Return left margin as an optimal point
    return xLeft 

# Gold section search in given direction
# Input: starting point, direction orth, object functuion procedure and accuracy
def gold_section_d(x0, dirVec, func, eps = 1.e-5):

    # Apply Svenn algorithm for interval search
    step = 0.1
    xLeft, xRight = svenn.svenn_d(x0, dirVec, func, step)

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
