% Flatcher-Reeves method

clear

global NEOF;

% Build a contour plot of the objective function
xMin = -4;
xMax = 0;
yMin = 0;
yMax = 4;
stepx = (xMax-xMin)/100;
stepy = (yMax-yMin)/100;

coord = [xMin:stepx:xMax; yMin:stepy:yMax];
nPoints = size(coord, 2);
ofun = zeros(nPoints);
for i = 1:nPoints
    for j=1:nPoints
        ofun(i,j) = of([coord(1,j),coord(2,i)]);
    end
end
hold on
contour(coord(1,:), coord(2,:), ofun);
% For Rozenbrock function
% contour(coord(2,:), coord(1,:), ofun, [1.e-2, 1.e-1, 5.e-1, 1.0, 2.0]);
% -----------------------------------------------------------

EPS = 1.e-4;
x0 =  [-1, 1];
point = zeros(2,10);
progress = zeros(1,10);
NEOF = 0;

% initial step
x = x0;
point(:,1) = x;
[fun, grad] = of(x);
dirVect = -grad;
normGradPrev = norm(grad);

for i=1:9
    xNew = gold_section(x, dirVect,  EPS);
    point(:,i+1) = xNew;
    progress(i) = norm(xNew - x);
    [fun, grad] = of(xNew);
    if (norm(xNew-x) < EPS)
        break
    end
    normGradNew = norm(grad);
    x = xNew;
    dirVect = -grad + (normGradNew/normGradPrev)^2 * dirVect;
    normGradPrev = normGradNew;
end

xOpt = xNew;
plot(point(1,1:i+1), point(2,1:i+1));
hold off

%progress(0, x0);
% for i=1:10
%     x1 = gold_section(x0, d1, EPS);
%     x2 = gold_section(x1, d2, EPS);
%     x3 = gold_section(x2, d1, EPS);
%     
%     point(3*i-1,:) = x1;
%     point(3*i,:)   = x2;
%     point(3*i+1,:) = x3;
%     
%     gradNew = x3 - x1;
%     plot([x1(1), x3(1)], [x1(2), x3(2)])
%     xOpt = gold_section(x3, gradNew, EPS);
%     progress(i, xOpt);
%     if norm(xOpt - x1) < EPS
%         break
%     end
%     x0 = xOpt;
%     d1 = d2;
%     d2 = gradNew;
% end
% 
% plot(point(:,1), point(:,2));
% hold('off')
