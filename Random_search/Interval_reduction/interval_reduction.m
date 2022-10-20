% Random search with interval reduction
% Test problem based on different functions of 2 variables
clear

global numberOFestimations

numberOFestimations = 0; % beeing reset to zero after each set calculation
KOCF = 0; % general number of estimations

% check wether x is localized inside given range or not
isInRange = @(x, xlow, xhigh) ...
    x(1) >= xlow(1) && x(1) <= xhigh(1) && ...
    x(2) >= xlow(2) && x(2) <= xhigh(2);

% func = 'griewank';
% 
% xmin = [-5; -5];
% xmax = [ 5;  5];


% func = 'schwefel';
% 
% xmin = [0; 0];
% xmax = [1000;  1000];


func = 'shubert';

xmin = [-2; -2];
xmax = [ 1;  1];

setSize = 100;
nSets = 10;

xlow = xmin;
xhigh = xmax;
width = xhigh - xlow;

% initial point and OF threshhold level
centralPoint = (xhigh + xlow)/2;
fThr = feval(func, centralPoint);



for set=1:nSets
    % contour plot of the OF
    step = (xmax - xmin)/100;
    coord = [xmin(1):step(1):xmax(1); xmin(2):step(2):xmax(2)];
    nPoints = size(coord, 2);
    ofun = zeros(nPoints);
    for i = 1:nPoints
        for j=1:nPoints
            ofun(i,j) = feval(func, [coord(1,j),coord(2,i)]);
        end
    end
    hold off
    contour (coord(1,:), coord(2,:), ofun)
    hold on
    % we don't need to cacculate OF calls during function plotting
    numberOFestimations = 0;

    % prelocation
    arg = zeros(2, setSize);
    of = zeros(1, setSize);
    nSucc = 0;
    
    for i=1:setSize
        arg(:,i) = centralPoint + [rand-0.5; rand-0.5].*width;
        if isInRange(arg(:,i), xlow, xhigh)
            of(i) = feval(func, arg(:,i));
            if of(i)<minimal
                minimal = of(i);
                bestPoint = i;
            end
        else
            % It never should be reached
            of(i) = Inf(1);
        end
    end
    
    KOCF = KOCF + numberOFestimations;

    if minimal < optim
        % renew the central point and compress the search area
        optim = minimal;
        optimPoint = arg(:,bestPoint);
        centralPoint = optimPoint;
        width = (1-eps)*width;
        xlow  = centralPoint - width/2;
        xhigh = centralPoint + width/2;
        % check and correct the ranges
        if xlow(1) < xmin(1)
            xlow(1) = xmin(1);
        end
        if xlow(2) < xmin(2)
            xlow(2) = xmin(2);
        end
        if xhigh(1) > xmax(1)
            xhigh(1) = xmax(1);
        end
        if xhigh(2) > xmax(2)
            xhigh(2) = xmax(2);
        end
        xOpt = arg(:,bestPoint);
        minimal = Inf(1);
        bestPoint = 0;
        % once again correct the central point and width
        centralPoint = (xlow + xhigh)/2;
        width = xhigh - xlow;
    end
    plot(xOpt(1), xOpt(2),'r*')
    pause(2)
end

fprintf("-----------------------------------------------\n");
fprintf("Random search:\n");
fprintf("Best point [%12.5g  %12.5g] of = %12.5g \n", xOpt, optim);
