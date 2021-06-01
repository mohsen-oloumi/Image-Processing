import cv2
from matplotlib import pyplot as plt
import matplotlib
import numpy as np 
img = cv2.imread('brain.jpg',0)

histr = cv2.calcHist([img],[0],None,[256],[0,256])

plt.plot(histr)
plt.show()

#############################2a
def lingray(x, a=None, b=None):
 
    if a == None:
        a = np.min(x)
    if b == None:
        b = np.max(x)
    return 255.0 * (x-float(a))/(b-a)

new_image_data = lingray(img)
new_image_min = 0.
new_image_max = np.max(new_image_data)
matplotlib.pyplot.imshow(new_image_data, vmin = new_image_min, vmax = new_image_max, cmap ='gray')  
matplotlib.pyplot.show() 
#############################2b
img = cv2.imread('brain.jpg',0)
log_img = np.uint8(np.log1p(img))
thresh = 1
img_2 = cv2.threshold(log_img , thresh , 255 , cv2.THRESH_BINARY)[1]

new_image_min = 0.
new_image_max = np.max(img_2)
matplotlib.pyplot.imshow(img_2, vmin = new_image_min, vmax = new_image_max, cmap ='gray')  
matplotlib.pyplot.show() 
##############################
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
new_image_min = 0.
new_image_max = np.max(res)
matplotlib.pyplot.imshow(res, vmin = new_image_min, vmax = new_image_max, cmap ='gray')  
matplotlib.pyplot.show() 