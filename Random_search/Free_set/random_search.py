import numpy as np
from random import random
from coordinate_descent import coordinate_descent


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


number_of_estimations = 0
func = 'griewank'
x_min = [-5, -5]
x_max = [5, 5]
width = [x_max[0] - x_min[0], x_max[1] - x_min[1]]
arg_abs_min = [0.0, 0.0]

# func = 'schwefel'
# x_min = [-500, -500]
# x_max = [ 500,  500]
# width = [x_max[0] - x_min[0], x_max[1] - x_min[1]]
# arg_abs_min = [420.9687, 420.9687]

n_points = 1000

list_of_args = [[0, 0] for i in range(n_points)]
obj_fun = np.zeros(n_points)

minimal = np.inf
best_point = 0

for i in range(n_points):
    list_of_args[i] = [x_min[0] + random() * width[0], x_min[1] + random() * width[1]]
    obj_fun[i] = griewank(list_of_args[i])
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

x_opt = coordinate_descent(griewank, list_of_args[best_point], 1.e-5)
f_opt = griewank(x_opt)

print(f'Optimal solution found: [{x_opt[0]:12.5g}  {x_opt[1]:12.5g}] of = {f_opt:12.5g}')
print(f'Total number of OF estimations: {number_of_estimations:5d}')
print('-----------------------------------------------')
#
#
# % Plot contours of the function and evaluated points
# x1Grid = xmin(1):width/100:xmax(1);
# x2Grid = xmin(2):width/100:xmax(2);
# nPoints1 = length(x1Grid);
# nPoints2 = length(x2Grid);
# objFunGrid = zeros(nPoints1,nPoints2);
#
# for i=1:nPoints1
#     for j=1:nPoints2
#         objFunGrid(i,j) = feval(func, [x1Grid(i), x2Grid(j)]);
#     end
# end
#
# hold on
# contour3(x2Grid, x1Grid, objFunGrid)
# plot(arg(2,:), arg(1,:), 'LineStyle','none','Marker', 'o')
# plot(arg(2,bestPoint), arg(1,bestPoint), 'LineStyle','none','Marker', 'o', 'Color', 'r')
# plot(xOpt(2), xOpt(1), 'LineStyle','none','Marker', 'x', 'Color', 'r')
# line([arg(2,bestPoint), xOpt(2)], [arg(1,bestPoint), xOpt(1)])
# hold off
