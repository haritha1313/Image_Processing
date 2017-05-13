# -*- coding: utf-8 -*-
"""
Created on Sat May 13 09:52:57 2017

@author: DELL NOTEBOOK
"""

import cv2
import numpy as np

img_bgr=cv2.imread('template.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template =cv2.imread('match.jpg',0)
w, h = template.shape[::-1]

res=cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold=0.8
loc=np.where(res>=threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)

cv2.imshow('detect', img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()