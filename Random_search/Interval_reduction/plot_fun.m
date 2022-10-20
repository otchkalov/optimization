clear
% Build a contour (or 3D) plot of the objective function

% func = 'schwefel';
% 
% argMin = -500;
% argMax = 500;
% step = 5;

% func = 'griewank';
% 
% argMin = -5;
% argMax = 5;
% step = 0.05;

func = 'shubert';

argMin = -2;
argMax = 1;
step = 0.01;

coord = [argMin:step:argMax; argMin:step:argMax];
nPoints = size(coord, 2);
ofun = zeros(nPoints);
for i = 1:nPoints
    for j=1:nPoints
        ofun(i,j) = feval(func, [coord(1,j),coord(2,i)]);
    end
end

surface (coord(1,:), coord(2,:), ofun)
% contour (coord(1,:), coord(2,:), ofun)