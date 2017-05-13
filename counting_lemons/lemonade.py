# -*- coding: utf-8 -*-
"""
Created on Sat May 13 12:22:23 2017

@author: DELL NOTEBOOK
"""

import numpy as np
import cv2

img = cv2.imread('lemons.jpeg')
gray = cv2.imread('lemons.jpeg',0)

ret,thresh = cv2.threshold(img,10,255,1)

#contours,h = cv2.findContours(thresh,1,2)

#cv2.imshow('contours',contours)
cv2.imshow('img', thresh)
cv2.imshow('img1', img)
cv2.imshow('gray', gray)


cv2.waitKey(0)
cv2.destroyAllWindows()