Img=imread('lena_ori.tiff');
Threshold=256;
for i=1:Threshold
    y=blkproc(Img,[8 8],'dct2');
    yy=blkproc(y,[8 8],'mask4',i);
    yq=blkproc(yy,[8,8],'idct2');
    yq=im2uint8(yq);
    MSE(i)=mean(mean((Img-yq).^2));
    disp(MSE(i))
end

