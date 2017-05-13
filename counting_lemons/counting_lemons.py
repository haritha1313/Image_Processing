# -*- coding: utf-8 -*-
"""
Created on Sat May 13 15:00:34 2017

@author: DELL NOTEBOOK
"""

import cv2
import numpy as np
import time
a=time.clock()

img = cv2.imread('lemons.jpeg')

hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
lower_yellow = np.array([20,0,0])
upper_green=np.array([70,255,255])
    
mask=cv2.inRange(hsv, lower_yellow, upper_green)
res=cv2.bitwise_and(img, img, mask=mask)                #masking for yellow-green color range

img1=cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
img2=cv2.GaussianBlur( img1, (9, 9), 2 )                #blur to remove noise
circles = cv2.HoughCircles(img2,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=20,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
c=0
for i in circles[0,:]:
    cv2.circle(res,(i[0],i[1]),i[2],(0,255,0),2)        #outer circle
    cv2.circle(res,(i[0],i[1]),2,(0,0,255),3)           #center of circle
    c=c+1                                               #counting lemons
    
print "No: of lemons %d = "%c
#cv2.imshow('circles',res)

cv2.imshow('detected circles',res)
b=time.clock()
print "Completed in time %d ms" % ((b-a)*1000)


cv2.waitKey(0)
cv2.destroyAllWindows()