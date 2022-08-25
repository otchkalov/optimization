function [ phi ] = func( x )
%FUNC Calculate the object function value for a given x point

% Simple quadratic function
phi = x(1)^2 + x(2)^2;
end

