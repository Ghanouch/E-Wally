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
            cap = cv2.VideoCapture()
        print("WAITING FOR A PERSON TO START THE GAME")
        ret, frame = cap.read()
        
            # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            
        if(fd.is_face_detected(gray)):
            cap.release()
            cv2.destroyAllWindows()  
                #time to wait after each process :
            wait = 4000
                
            while(oh.is_switch_on() == True):
                utils.wait_for(wait)
                cap = cv2.VideoCapture(0)
                    # Capture frame-by-frame
                ret, frame = cap.read()
                
                    # Our operations on the frame come here
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    
                    
                if(fd.is_face_detected(gray)):
                        #transform image :
                    print("PERSON DETECTED")
                    image = tf.transform_image(gray)
                    cv2.imshow('image',gray)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                        #process
                    data = em.get_emotion(image)
                    emotion_result = rp.process_result(data)
                    print(emotion_result)
                        
                    oh.set_openhab_emotion_text(emotion_result)
                
                cap.release()
                cv2.destroyAllWindows()
            print("SERVER STOPPED...")
            break

while(True):
    if(oh.is_switch_on() == True):
        start_server()
                    


# When everything done, release the capture
