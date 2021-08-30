%  Probelm 4
clc;
clear;
close all;

format long
%
sn1=0;
sn2=0;
sn3=0;
sn2a=0;
sn2b=0;

for n=1:1e+6
    sn1=sn1-(2*n-1)/(2*n)+(2*n)/(2*n+1);
    sn2a=sn2a+(2*n-1)/(2*n);
    sn2b=sn2b+(2*n)/(2*n+1);
    sn3=sn3+1/((2*n)*(2*n+1));
    %
    xx(n)=n;
    sn1sum(n)=sn1;
    sn2sum(n)=sn2b-sn2a;
    sn3sum(n)=sn3;
    err1(n)=abs((sn1-sn3)/sn3);
end

S=[sn2a sn2b];

display('      sn1                 sn2               sn3')
fprintf('%15.12e %15.12e %15.12e\n', sn1, sn2b-sn2a, sn3)

figure (1);
loglog(xx,err1,'-r');
xlabel('N');
ylabel('relative error');
grid on;
