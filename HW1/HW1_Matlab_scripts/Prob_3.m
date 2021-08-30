%Problem 3

% evaluate
%x1=(-b+sqrt(b^2-4*a*c))/(2*a);
%x2=(-b-sqrt(b^2-4*a*c))/(2*a);
%x1p=-2*c/(b+sqrt(b^2-4*a*c));
%x2p=-2*c/(b-sqrt(b^2-4*a*c));

%part a, b and c

 clc;clear;close all;
 format long
 a=1;
 b=1;
 for n = 1:20
      c=10^(-n);
      x1=(-b+sqrt(b^2-4*a*c))/(2*a);
      x2=(-b-sqrt(b^2-4*a*c))/(2*a);
      x1p=-2*c/(b+sqrt(b^2-4*a*c));
      x2p=-2*c/(b-sqrt(b^2-4*a*c));
      X(n,:)=[x1 x1p  x2  x2p ];
 end
 
 display ('x1, x1p, x2, x2p')
 for n = 1:20
     fprintf('% 5d %15.12e %15.12e %15.12e %15.12e\n',n, X(n,:))
 end

%At iteration n=17, x2p became infinite. 
%so n=1:16 is used for the evaluation of part d

%part d
for n =1:16
     c=10^(-n);
     xx(n)=4*a*c;
     y1(n)=[abs((X(n,1)-X(n,2))/X(n,2))];  % take x1p as accurate value
     y2(n)=[abs((X(n,4)-X(n,3))/X(n,3))];  % take x2  as accurate value
end
figure
loglog(xx,y1,'-rd')
hold on
loglog(xx,y2,'--bs')
xlabel('4ac')
ylabel('Relative error')
legend('Relative error for x1','Relative error for x2')
grid on
%end part d

