function [y]=mask4(x,Threshold)
mask =zeros(8,8);
mask(abs(x) > Threshold)=1;
   
y=mask.*x;
y=im2double(y);
end