% Problem 2

% evaluation of polynomial

clear;clc;close all;
x = [0.995:0.0001:1.005]; 
poly1 = (x-1.0).^6;
poly2 = x.^6-6*x.^5+15*x.^4 -20*x.^3+15*x.^2-6*x+1;
plot(x,poly1,'b--',x,poly2,'r-');
title('Computer Problem 2 - Computing (x-1)^6');
xlabel('x'); ylabel('p(x)'); 
legend('compact formula','expanded formula');