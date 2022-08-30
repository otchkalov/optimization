function [x_new] = rosenbrock_method ( x, init_step)

s1 = [1 0];
s2 = [0 1];

lambda = init_step * ones(2, 1);

x_new = coordinate_search(x, lambda);

end