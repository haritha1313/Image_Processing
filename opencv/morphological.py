# -*- coding: utf-8 -*-
"""
Created on Sat May 13 09:22:26 2017

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
    
    kernel=np.ones((5,5), np.uint8)
    erosion=cv2.erode(mask, kernel, iterations=1)
    
    dilation=cv2.dilate(mask, kernel, iterations=1)
    
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    cv2.imshow('erode', erosion)
    cv2.imshow('dilate', dilation)
    cv2.imshow('epening', opening)
    cv2.imshow('closing', closing)
    
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
    ret, frame=cap.read()
cv2.destroyAllWindows()
cap.release()