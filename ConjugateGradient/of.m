% of.m
% Calculate object function value

function [fun, dfdx] = of(x)

global NEOF;
NEOF = NEOF + 1;

% Quadratic function
% fun = 4*x(1)^2 + 3*x(2)^2 - 4*x(1)*x(2) + x(1);
% dfdx(1) = 8*x(1) - 4*x(2) + 1;
% dfdx(2) = 6*x(2) - 4*x(1);

% Himmelblau's function
% argMin = -4; argMax = -2;
fun = (x(1)^2 + x(2) - 11)^2 + (x(1) + x(2)^2 - 7)^2;
dfdx(1) = 2*(x(1)^2 + x(2) - 11)*2*x(1) + 2*(x(1) + x(2)^2 - 7);
dfdx(2) = 2*(x(1)^2 + x(2) - 11) + 2*(x(1) + x(2)^2 - 7)*2*x(2);

% Rozenbrock function
% x1=[-1:0.1:3];
% y1=[-2:0.1:2];
% fun = 100*(x(2)-x(1)^2)^2 +(1-x(1))^2;
% dfdx(1) = -400*(x(2)-x(1)^2)*x(1) - 2*(1-x(1));
% dfdx(2) = 200*(x(2)-x(1)^2);

end
