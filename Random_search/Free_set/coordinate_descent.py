import numpy as np
import gold_section as gs


def coordinate_descent(func, x_init, eps):

    x_0 = x_init.copy()
    x_opt = x_init.copy()
    for i in range(10):
        dir_vec = [1, 0]
        x_1 = gs.gold_section_d(x_0.copy(), dir_vec, func, eps)
        if np.abs(x_1[0] - x_0[0]) < eps:
            x_opt = x_1
            break
    
        dir_vec = [0, 1]
        x_2 = gs.gold_section_d(x_1.copy(), dir_vec, func, eps)
        if np.abs(x_2[1] - x_1[1]) < eps:
            x_opt = x_2
            break
        else:
            x_0 = x_2
    return x_opt
