# -*- coding: utf-8 -*-
"""
Created on Fri May 12 20:51:43 2017

@author: DELL NOTEBOOK
"""

import numpy as np
import cv2

img=cv2.imread('kinleywaterbottel.jpg', cv2.IMREAD_COLOR)
img[130,130]=[255,255,255]
px=img[130,130]
print(px)

#img[300:400, 80:200] = [255,255,255]

label = img[300:400, 80:200]

img[0:100, 0:120] =label
cv2.imshow('age',img)
cv2.waitKey(0)
cv2.destroyAllWindows()