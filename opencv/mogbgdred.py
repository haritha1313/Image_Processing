# -*- coding: utf-8 -*-
"""
Created on Sat May 13 11:12:38 2017

@author: DELL NOTEBOOK
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fgbg=cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame= cap.read()
    fgmask= fgbg.apply(frame)
    
    cv2.imshow('original', frame)
    cv2.imshow('fg', fgmask)
    
    k=cv2.waitKey(30) & 0xFF
    if k==27:
        break
    
cap.release()
cv2.destroyAllWindows()