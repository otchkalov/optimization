function [ phi ] = schwefel( x )
%FUNC Calculate object function at particular point x

%phi = (x(1)^2 + x(2) - 11)^2 + (x(1) + x(2)^2 - 7)^2;

% SCHWEFEL FUNCTION
% Search interval [-500; 500]
% Global minimum f(x)=0 at x = [420.9687; 420.9687] 

global numberOFestimations
numberOFestimations = numberOFestimations+1;

sum = 0;
for i = 1:2
	sum = sum + x(i)*sin(sqrt(abs(x(i))));
end

phi = 418.9829*2 - sum;

end


