% Problem 1
% Finite difference approximation to derivative

clc;
clear;
close all;

true_value = sec(1.0)^2; 

x = 1.0; 
k = [0:16]; 
h = 1.0./(10.^k);

forward_diff = abs((tan(x+h)-tan(x))./h);
error_a = abs(forward_diff-true_value);

centered_diff = abs((tan(x+h)-tan(x-h))./(2*h));
error_b = abs(centered_diff-true_value);

loglog(h,error_a,'b-',h,error_b,'r--');
grid;
xlabel('stepsize h'); 
ylabel('magnitude of error');
legend('forward difference','centered difference');