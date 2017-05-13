# -*- coding: utf-8 -*-
"""
Created on Fri May 12 22:47:54 2017

@author: DELL NOTEBOOK
"""

import cv2
import numpy as np

cap=cv2.VideoCapture(0)
ret, frame=cap.read()
while(ret):
    ret, frame=cap.read()
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([150,150,50])
    upper_red=np.array([180,255,150])
    
    mask=cv2.inRange(hsv, lower_red, upper_red)
    res=cv2.bitwise_and(frame, frame, mask=mask)
    
    kernel=np.ones((15,15), np.float32)/255
    smoothed=cv2.filter2D(res, -1, kernel)
    blur=cv2.GaussianBlur(res, (15,15), 0) 
    cv2.imshow('frame', frame)
    #cv2.imshow('smooth', smoothed)
    cv2.imshow('res', res)
    cv2.imshow('blur',blur)
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
    ret, frame=cap.read()
cv2.destroyAllWindows()
cap.release()