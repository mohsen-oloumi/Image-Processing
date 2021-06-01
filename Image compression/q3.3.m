% ******************************************************************
% * MATLAB Script file for demonstration of DCT representation of images *
% * You should find out how to use “blkproc” by on-line help in matlab.
% ******************************************************************

close all; clc; clear all
% usage : dctquant('h:\el593\exp10\lena.img',256,256); (WYT: please verify)
% Note, dctquant calls subfunctions mask2()
% Img=fread(fopen(FileName),[dx,dy]);
I=imread('girl.tif');
img=(im2double(I));
L=16;
for i=1:L
    y=blkproc(img,[8 8],'dct2');
    yy=blkproc(y,[8 8],'mask3',i);
    yq=blkproc(yy,[8,8],'idct2');
    MSE(i)=mean(mean((img-yq).^2));
    MSE(i)
end
