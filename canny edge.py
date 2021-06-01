import numpy as np
import cv2
from skimage.transform import (hough_line, hough_line_peaks,
                               probabilistic_hough_line)
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import euclidean_distances
from scipy.spatial import distance
import imutils


def load_img_gray (path):
    return cv2.imread(path,0)
def detect_edge_with_canny(img,t1,t2):
    return cv2.Canny(img,t1,t2)

def hough_transform(image ,edges ,t ):
    lines = probabilistic_hough_line(edges, threshold=t, line_length=5,
                                 line_gap=3)
    return edges

hists_original=[]
for i in range(1,21):
    path = 'rotated/'+str(i)+'.jpg'
    src = load_img_gray(path)
    edgeImage = detect_edge_with_canny(src,i*1.2,i*1.2)
    houghTransform = hough_transform(src , edgeImage,2)
    hist,bins = np.histogram(src.ravel(),11,[0,360])
    hists_original.append(hist)

    
hists_rotated=[]
for i in range(1,21):
    path = 'original/'+str(i)+'.jpg'
    src = load_img_gray(path)
    edgeImage = detect_edge_with_canny(src,i*1.2,i*1.2)
    houghTransform = hough_transform(src , edgeImage,2)
    hist,bins = np.histogram(src.ravel(),11,[0,360])
    hists_rotated.append(hist)
mini = 100000000
index = 0
dic = {}
for i in range(len(hists_rotated)):
    for j in range(len(hists_original)):
        dist = distance.euclidean(hists_rotated[i],hists_original[j])

        if mini > dist:
            mini = dist
            index = j
    #print i ,index , mini 
    dic[i]=index
    mini = 100000000
    index = 0
mindist = 100000000
for i in dic :
    print i
    image = cv2.imread('rotated/'+str(i+1)+'.jpg')
    index = 0
    for angle in np.arange(0, 360, 11):
        #cv2.imshow("Rotated (Correct)", image)
        #cv2.waitKey(0)
        rotated = imutils.rotate(image, angle)
        
        hist,bins = np.histogram(rotated.ravel(),11,[0,360])
        dist = distance.euclidean(hist,hists_original[dic[i+1]])
        if dist < mindist :
            mindist = dist
            index = angle
    print i , index , mindist
    cv2.imshow("Rotated (Correct)", imutils.rotate(image, index))
    cv2.waitKey(0)
    mindist = 100000000
    index = 0