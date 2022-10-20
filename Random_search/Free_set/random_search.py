import numpy as np
from random import random
from coordinate_descent import coordinate_descent
import plotter


def griewank(xx):
    # Griewank function
    # INPUT:
    # xx = [x1, x2, ..., xd]

    global number_of_estimations
    number_of_estimations = number_of_estimations + 1

    size_of_xx = len(xx)
    summ = 0
    prodd = 1

    for ii in range(size_of_xx):
        xi = xx[ii]
        summ = summ + xi**2 / 4000
        prodd = prodd * np.cos(xi / np.sqrt(ii + 1))

    return (summ - prodd + 1) * 1.e3


def schwefel(xx):
    # SCHWEFEL FUNCTION
    # Search interval[-500; 500]
    # Global minimum f(x) = 0 at x = [420.9687; 420.9687]
    # INPUT:
    # xx = [x1, x2]

    global number_of_estimations
    number_of_estimations = number_of_estimations + 1

    summ = 0
    for ii in range(2):
        summ = summ + xx[ii] * np.sin(np.sqrt(np.abs(xx[ii])))

    return 418.9829 * 2 - summ


number_of_estimations = 0

func = 'griewank'
# func = 'schwefel'

if func == 'griewank':
    def fun(xx):
        return griewank(xx)
    x_min = np.array([-5, -5])
    x_max = np.array([5, 5])
    arg_abs_min = np.array([0.0, 0.0])
else:
    def fun(xx):
        return schwefel(xx)
    x_min = np.array([-500, -500])
    x_max = np.array([500, 500])
    arg_abs_min = np.array([420.9687, 420.9687])

n_points = 500

list_of_args = np.zeros([n_points + 1, 2])
obj_fun = np.zeros(n_points)

minimal = np.inf
best_point = 0
width = np.subtract(x_max, x_min)

for i in range(n_points):
    # We need to call random() twice to get different values for 2 arguments
    delta = np.array([random(), random()])
    list_of_args[i] = np.add(x_min, np.multiply(delta, width))
    obj_fun[i] = fun(list_of_args[i])
    if obj_fun[i] < minimal:
        minimal = obj_fun[i]
        best_point = i

print('-----------------------------------------------')
print('Random_search search:')
print(f'Best point [{list_of_args[best_point][0]:12.5g},  '
      f'{list_of_args[best_point][0]:12.5g}] of = {obj_fun[best_point]:12.5g}')
distance = np.sqrt((list_of_args[best_point][0] - arg_abs_min[0])**2 +
                   (list_of_args[best_point][1] - arg_abs_min[1])**2)
print(f'Distance {distance:12.5g}')

x_opt = coordinate_descent(fun, list_of_args[best_point], 1.e-5)
f_opt = fun(x_opt)

list_of_args[n_points] = x_opt

print(f'Optimal solution found: [{x_opt[0]:12.5g}  {x_opt[1]:12.5g}] of = {f_opt:12.5g}')
print(f'Total number of OF estimations: {number_of_estimations:5d}')
print('-----------------------------------------------')


# Plot contours of the function and evaluated points
n_ticks = 500
x1_list = np.linspace(x_min[0], x_max[0], n_ticks)
x2_list = np.linspace(x_min[1], x_max[1], n_ticks)
obj_fun_grid = [np.zeros(n_ticks) for i in range(n_ticks)]

for i in range(n_ticks):
    for j in range(n_ticks):
        obj_fun_grid[i][j] = griewank([x1_list[i], x2_list[j]])

plotter.plot_graph_p1(x1_list, x2_list, obj_fun_grid, list_of_args, best_point)
