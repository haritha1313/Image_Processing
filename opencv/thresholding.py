# -*- coding: utf-8 -*-
"""
Created on Fri May 12 21:41:13 2017

@author: DELL NOTEBOOK
"""

import cv2
import numpy as np

img=cv2.imread('bookpage.jpg')

retval, threshold= cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
garyscaled=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

retval2, threshold2 = cv2.threshold(garyscaled, 12,255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(garyscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115,1)
cv2.imshow('óriginal', threshold)
cv2.imshow('threshold',threshold2)
cv2.imshow('gaus',gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()