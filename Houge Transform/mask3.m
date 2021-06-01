function [y]=mask3(x,L)
mask=zeros(8,8);
if L>=1 
    mask(1,1)=1;
end
if L>=2
    mask(1,2)=1;
end
if L>=3
    mask(2,1)=1;
end
if L>=4
    mask(1,3)=1;
end
if L>=5
    mask(2,2)=1;
end
if L>=6
    mask(3,1)=1;
end
if L>=7
    mask(1,4)=1;
end
if L>=8
    mask(2,3)=1;
end
if L>=9
    mask(3,2)=1;
end
if L>=10
    mask(4,1)=1;
end
if L>=11
    mask(1,5)=1;
end
if L>=12
    mask(2,4)=1;
end
if L>=13
    mask(3,3)=1;
end
if L>=14
    mask(4,2)=1;
end
if L>=15
    mask(5,1)=1;
end
if L>=16
    mask(1,6)=1;
end    
y=mask.*x;
end