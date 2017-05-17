# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:39:15 2017

@author: DELL NOTEBOOK
"""

import cv2
import numpy as np
import time
from skimage.measure import regionprops


a=time.clock()
image = cv2.imread('lemons.jpeg')

hsv= cv2.cvtColor(image, cv2.COLOR_BGR2HSV )                #selecting only yellow-green region
lower_yellow = np.array([20,90,40])
upper_green=np.array([70,255,255])
mask=cv2.inRange(hsv, lower_yellow, upper_green)
maskin=cv2.bitwise_not(mask)
res=cv2.bitwise_and(image, image, mask=mask)
gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY) 

gray=cv2.GaussianBlur(gray, (15,15), 0)

thim = cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 1 )  #applying threshold

im, contours, hierarchy = cv2.findContours(thim, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour2=[]
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area>200:                                            #contour mapping above minimal area specified
        contour2.append(cnt)
        
contor=cv2.drawContours(thim.copy(), contour2, -1, (0,255,0), 1)
#formap = cv2.bitwise_not(thim-contor)
formap = thim-contor
formap = cv2.Canny(formap,100,200)                          #edges marked
formap = cv2.bitwise_not(formap)
kernel = np.ones((3,3),np.uint8)
#mask2 = cv2.erode(mask,kernel,iterations = 1)
#cv2.imshow('érose',mask2)
"""
formap = cv2.erode(formap,kernel,iterations = 6)

newmap = cv2.dilate(formap,kernel,iterations =6)

newmap=cv2.bitwise_and(newmap, mask)
"""

newmap=cv2.bitwise_and(formap, mask)

sure_bg = cv2.dilate(newmap,kernel,iterations=1)            #sure background

dist_transform = cv2.distanceTransform(newmap,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.2*dist_transform.max(),255,0)     #sure foreground

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)                     #unknown areas

ret, markers = cv2.connectedComponents(sure_fg)

markers = markers+1

markers[unknown==255] = 0                                   #unknown regions marked 0
markers = cv2.watershed(image,markers)                      #watershed algorithm
image[markers == -1] = [255,0,0]
regions = regionprops(markers)
regions = [r for r in regions if r.area > 100]

print 'Number of coins:', len(regions) - 1
cv2.imshow('marked',image)

b=time.clock()
print "Completed in time %d ms" % ((b-a)*1000)              #avg time of 24.66 ms
cv2.waitKey(0)
cv2.destroyAllWindows()