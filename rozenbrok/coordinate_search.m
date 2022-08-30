function [ x_new ] = coordinate_search( x, direction_vectors, init_step )
%FUNC Coordinate test search for Rozenbrock procedure

n1 = size(x);
n = n1(2);
clear n1;

alpha = 3.0;
beta = -0.5;

x_new = x; 
phi_accepted = func(x);

lambda_mod = init_step;

step_result = zeros(1, n);
search_completed = ones(1, n);
while (step_result ~= search_completed)
    for i=1:n
        step = direction_vectors(i,:)*lambda_mod(i);
        phi_new = func(x_new + step);
        if phi_new < phi_accepted
            x_new = x_new + step;
            phi_accepted = phi_new;
            lambda_mod(i) = alpha*lambda_mod(i);
            step_result(i) = -1;
        else
            lambda_mod(i) = beta*lambda_mod(i);
            if step_result(i) == -1
                step_result(i) = 1;
            end
        end
    end
end

end