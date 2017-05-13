# -*- coding: utf-8 -*-
"""
Created on Sat May 13 11:23:06 2017

@author: DELL NOTEBOOK
"""

import cv2
import numpy as np

face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
num=0
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces)>num:
        num=len(faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+h]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)
            
    cv2.imshow('img', frame)
    k=cv2.waitKey(30) & 0xFF
    if k==27:
        break
print(num)
cap.release()
cv2.destroyAllWindows()
    
