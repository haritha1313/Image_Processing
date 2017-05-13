# -*- coding: utf-8 -*-
"""
Created on Sat May 13 09:41:37 2017

@author: DELL NOTEBOOK
"""

import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx=cv2.Sobel(frame, cv2.CV_64F,1,0,ksize=5)
    sobely=cv2.Sobel(frame, cv2.CV_64F,0,1,ksize=5)
    
    edges=cv2.Canny(frame,100,200)
    cv2.imshow('original', frame)
    cv2.imshow('lap', laplacian)
    cv2.imshow('sobx', sobelx)
    cv2.imshow('soby', sobely)
    cv2.imshow('edge', edges)
    
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()