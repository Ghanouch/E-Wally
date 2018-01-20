# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 13:20:34 2018

@author: amine
"""

#face detection
import cv2
def is_face_detected(image):
    
    face_cascade = cv2.CascadeClassifier('/home/amine/projets/Emotions_project/lbpcascade_frontalface_improved.xml')
    faces_result = face_cascade.detectMultiScale(image, 1.3, 5)
    if(len(faces_result)!=0):
        return True
    return False
