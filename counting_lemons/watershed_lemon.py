# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:39:15 2017

@author: DELL NOTEBOOK
"""

import cv2
import numpy as np

import time
a=time.clock()
from skimage.measure import regionprops
image = cv2.imread('lemons1.jpg')

hsv= cv2.cvtColor(image, cv2.COLOR_BGR2HSV )
lower_yellow = np.array([20,90,40])
upper_green=np.array([70,255,255])

mask=cv2.inRange(hsv, lower_yellow, upper_green)
maskin=cv2.bitwise_not(mask)
res=cv2.bitwise_and(image, image, mask=mask)
gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY) 

gray=cv2.GaussianBlur(gray, (15,15), 0)

thim = cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 1 )

im, contours, hierarchy = cv2.findContours(thim, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour2=[]
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area>200:
        contour2.append(cnt)
        
contor=cv2.drawContours(thim.copy(), contour2, -1, (0,255,0), 1)
#formap = cv2.bitwise_not(thim-contor)
formap = thim-contor
formap = cv2.Canny(formap,100,200)
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
sure_bg = cv2.dilate(newmap,kernel,iterations=1)

cv2.imshow('sure',sure_bg)

dist_transform = cv2.distanceTransform(newmap,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.2*dist_transform.max(),255,0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

ret, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0
markers = cv2.watershed(image,markers)
image[markers == -1] = [255,0,0]
regions = regionprops(markers)
regions = [r for r in regions if r.area > 50]

print 'Number of coins:', len(regions) - 1
cv2.imshow('marked',image)

b=time.clock()
print "Completed in time %d ms" % ((b-a)*1000)
cv2.waitKey(0)
cv2.destroyAllWindows()