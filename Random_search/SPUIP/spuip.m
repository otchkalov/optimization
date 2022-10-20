% Random search with range reduction
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

xmin = [-2, -2];
xmax = [ 1,  1];

setSize = 100;
nSets = 10;
eps = 0.05;  % relative search tolerance
nSuccMin = 5;

xLow = xmin;
xHigh = xmax;
width = xHigh - xLow;

centralPoint = (xHigh + xLow)/2;
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

    % arrays prelocation
    argSucc = zeros(setSize, 2);
    ofSucc = zeros(setSize, 1);
    
    nSucc = 0;

    for i=1:setSize
        varpar = centralPoint + [rand-0.5, rand-0.5].*width;
        if isInRange(varpar, xLow, xHigh)
            of = feval(func, varpar);
            if of < fThr
                nSucc = nSucc + 1;
                argSucc(i,:) = varpar;
                ofSucc(i) = of;
                plot(varpar(1),varpar(2),'r.')
            else
                plot(varpar(1),varpar(2),'b.')
            end
        else
            % It never should be reached
            of(i) = Inf(1);
        end
    end
    
    if nSucc >= nSuccMin
        % correct ranges and threshhold value
        [xLow, xHigh] = bounds(argSucc(1:nSucc,:));
        fThr = min(ofSucc(1:nSucc));
        width = xHigh - xLow;
        centralPoint = (xHigh + xLow)/2;
    else
        %fThr = 1.5*fThr - 0.5*min(ofSucc(1:nSucc));
        fThr = fThr + 0.5*abs(fThr);
    end
    
    rectangle('Position',[xLow,width])
    pause(2)
            
    KOCF = KOCF + numberOFestimations;
end
