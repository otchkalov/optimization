"""
Conjugate gradient method
"""
import numpy as np
import gold_section as gs
import plotter
import numpy as np


def  func(x):
# Calculate object function value

    # Simple quadratic function
    # fun = (x[0] - 1)**2 + (x[1] - 1)**2 - x[0]*x[1]
    # fun = (x[0] - 1)**2 + (x[1] - 1)**2
    # fun = fun + np.random.uniform(-1, 1)

    # Himmelblau function
    fun = (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

    # Rastrigin function
    # fun = x[0]**2 + x[1]**2 - 10*(2 - np.cos( 2 * np.pi * x[0]) - np.cos( 2 * np.pi * x[1]))

    # Rosenbrock function
    # fun = 100*(x[1] - x[0]**2)**2 + (1 - x[0])**2

    # Ackley function
    # fun = -20 * np.exp( -0.2 * np.sqrt( 0.5 * (x[0]**2 + x[1]**2))) - \
    #     np.exp( 0.5 * (np.cos( 2 * np.pi * x[0]) + np.cos( 2 * np.pi * x[1]))) + np.e + 20

    return fun


def set_limits(func_name):
    switcher = {
        "quadratic": [[-4, 4], [-4, 4]],
        "Himmelblau": [[-5, 5], [-5, 5]],
        "Rasstrigin": [[-1, 1], [-1, 1]],
        "Rosenbrock": [[-2, 2], [-1, 3]],
        "Ackley": [[-4, 4], [-4, 4]],
    }
    limits = switcher.get(func_name, [[0, 0], [1, 1]])
    return limits[0], limits[1]

% Conjugate gradient method

clear

% Build a contour plot of the objective function
argMin = -0.2;
argMax = 0.1;
step = 0.01;

coord = [argMin:step:argMax; argMin:step:argMax];
nPoints = size(coord, 2);
ofun = zeros(nPoints);
for i = 1:nPoints
    for j=1:nPoints
        ofun(i,j) = of([coord(1,j),coord(2,i)]);
    end
end
hold on
contour(coord(2,:), coord(1,:), ofun);
% For Rozenbrock function
% contour(coord(2,:), coord(1,:), ofun, [1.e-2, 1.e-1, 5.e-1, 1.0, 2.0]);
% -----------------------------------------------------------


EPS = 1.e-4;
x0 = [0, 0];
point(1,:) = x0;
d1 = [1, 0];
d2 = [0, 1];
progress(0, x0);
for i=1:10
    x1 = gold_section(x0, d1, EPS);
    x2 = gold_section(x1, d2, EPS);
    x3 = gold_section(x2, d1, EPS);
    
    point(3*i-1,:) = x1;
    point(3*i,:)   = x2;
    point(3*i+1,:) = x3;
    
    gradNew = x3 - x1;
    plot([x1(1), x3(1)], [x1(2), x3(2)])
    xOpt = gold_section(x3, gradNew, EPS);
    progress(i, xOpt);
    if norm(xOpt - x1) < EPS
        break
    end
    x0 = xOpt;
    d1 = d2;
    d2 = gradNew;
end

plot(point(:,1), point(:,2));
hold('off')
