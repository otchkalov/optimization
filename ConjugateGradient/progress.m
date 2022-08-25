% progress.m
% Print the current stage of the optimization process

function [] = progress(iter,x) 

disp(['Iteration ', num2str(iter,3), '  x = [', num2str(x,7), '] ', 'of = ', num2str(of(x))])

end