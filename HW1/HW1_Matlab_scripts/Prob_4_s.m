%  Probelm 4

%
clc;
clear;
close all;

sn1=single(0);
sn2=single(0);
sn3=single(0);
sn2a=single(0);
sn2b=single(0);

n=single(0);

for n=1:1e+6
    sn1=sn1-single((2*n-1)/(2*n))+single((2*n)/(2*n+1));
    sn2a=sn2a+single((2*n-1)/(2*n));
    sn2b=sn2b+single((2*n)/(2*n+1));
    sn3=sn3+single(1/((2*n)*(2*n+1)));
    %
    xx(n)=n;
    sn1sum(n)=sn1;
    sn2sum(n)=sn2b-sn2a;
    sn3sum(n)=sn3;
    err1(n)=abs((sn1-sn3)/sn3);
   
end

S=[sn2a sn2b];
display('      sn1           sn2         sn3')
fprintf('%13.6e %13.6e %13.6e\n', sn1, sn2b-sn2a, sn3)

figure (2);
loglog(xx,err1,'-b');
xlabel('N');
ylabel('relative error');
grid on;
