import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread("ross.jpg", cv2.COLOR_BGR2GRAY)
cv2.imshow("Input", image)
image = cv2.medianBlur(image, 5)
cv2.imshow("Output", image)
cv2.waitKey(0)


img = image
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst)
plt.show()