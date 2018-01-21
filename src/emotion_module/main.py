# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 13:15:23 2018

@author: amine
"""

#main entry
import cv2
import utils
import face_detection as fd
import image_transform as tf
import emotion_api as em
import emotion_process as rp 
import openhab_emotion as oh



def start_server():
    print("SERVER STARTED...")
    cap = cv2.VideoCapture(0)
    
    while(True):
        if(cap.isOpened()==False):
            cap = cv2.VideoCapture(0)
        #print("WAITING FOR A PERSON TO START THE GAME")
        ret, frame = cap.read()
        # Display the resulting frame
        cv2.imshow('frame',frame)
        cv2.waitKey(1)
        #utils.wait_for(4000)
        wait = 2000
        res1 , res2 = fd.is_face_detected(frame)
        if(res1):
            for (x,y,w,h) in res2:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cap.release()
            cv2.destroyAllWindows()
            cap = cv2.VideoCapture(0)
            current_milli_time = utils.get_curent_time()
            while(utils.get_curent_time()-current_milli_time < wait or res1==False):
                ret, frame = cap.read()
                res1 , res2 = fd.is_face_detected(frame)
                for (x,y,w,h) in res2:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                cv2.imshow('frame',frame)
                cv2.waitKey(1)
                if(oh.is_switch_off()):
                    return
            image = tf.transform_image(frame)
            data = em.get_emotion(image)
            emotion_result = rp.process_result(data)
            print(emotion_result)
            oh.set_openhab_emotion_text(emotion_result)
            utils.wait_for(3000) #time for displaying on the led 
            if(oh.is_switch_off()):
                return
                

start_server()
                    


# When everything done, release the capture
