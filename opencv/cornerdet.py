# -*- coding: utf-8 -*-
"""
Created on Sat May 13 10:43:36 2017

@author: DELL NOTEBOOK
"""

import cv2
import numpy as np

img = cv2.imread('corners.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)


corners = cv2.goodFeaturesToTrack(gray, 100 , 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)
    
cv2.imshow('Corners', img)
cv2.waitKey(0)
cv2.destroyAllWindows()