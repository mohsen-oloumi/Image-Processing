I=imread('lena_ori.tiff');
img=(im2double(I));
y=blkproc(img,[8 8],'dct2');
yy=blkproc(y,[8 8],'mask2');
yq=blkproc(yy,[8,8],'idct2');
MSE=mean(mean((img-yq).^2));
MSE