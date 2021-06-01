TIFimg=imread('girl.tif');
TIFimg_gray=rgb2gray(TIFimg);
imwrite(TIFimg_gray,'girl.jpg','Mode','lossless')

JPGimg=imread('girl.jpg');
MSE = mean(mean((TIFimg_gray-JPGimg).^2));
disp(MSE);

for i=0:5:100
    imwrite(TIFimg_gray,'girl.jpg','Quality',i,'Mode','lossy');
    JPGimg=imread('girl.jpg');
    MSE=mean(mean((TIFimg_gray-JPGimg).^2));
    disp (MSE+"  "+i);
end
