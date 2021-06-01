import numpy as np
import cv2
import scipy.fftpack
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

# Load an color image in grayscale
img = cv2.imread('girl.tif',0)
def mse(vref, vcmp):
    r = np.asarray(vref, dtype=np.float64).ravel()
    c = np.asarray(vcmp, dtype=np.float64).ravel()
    return np.mean(np.fabs(r - c)**2)

def snr(vref, vcmp):
    dv = np.var(vref)
    with np.errstate(divide='ignore'):
        rt = dv/mse(vref, vcmp)
    return 10.0*np.log10(rt) 

def display_result(img, title = 'Image', show = 1):
    cv2.imshow(title, img)
    if show == 1:
        cv2.waitKey(0)
        cv2.destroyAllWindows()
np_image = np.asarray(img)
fft_image = np.fft.fft2(np_image)
magnitude = np.abs(fft_image)
phase = np.angle(fft_image)
plt.plot(magnitude)
plt.show()
plt.plot(phase)
plt.show()
dct_img = scipy.fftpack.dct(img)
img_shape = np.shape(dct_img)
Z = np.zeros((img_shape[0],img_shape[1]),dtype=int)
Z[0:int (img_shape[0]/2), 0:int (img_shape[1]/2)] = 1
dct_img = np.multiply(dct_img,Z)
idct_img = scipy.fftpack.idct(dct_img)
print snr (img,idct_img)