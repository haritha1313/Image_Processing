# -*- coding: utf-8 -*-
"""
Created on Fri May 12 20:20:10 2017

@author: DELL NOTEBOOK
"""

import numpy as np
import cv2

img = cv2.imread('kinleywaterbottel.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150,150), (255,0,0), 15)
cv2.rectangle(img, (25,25), (50,50), (255,255,255),5)
cv2.circle(img, (100,63), 50, (0,0,0), 1)

pts = np.array([[10,5],[20,30],[50,10],[20,50],[70,20]], np.int32)
#pts=pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (255,25,255), 4)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Hey opencv', (0,130), font, 1, (244,12,144), 2, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()