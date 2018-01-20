# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 14:16:30 2018

@author: amine
"""

#image transform 
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 22:23:32 2017

@author: Wall-e group
"""
import cv2
#not used
def take_picture():
    #define the size of the screen
    #init pygame
    pygame.init()
    pygame.camera.init()
    
    cam = pygame.camera.Camera("/dev/video0",(640,480))
    cam.start()
    image = cam.get_image()
    cam.stop()
    return image
#not used
def show_image(image):
    w = 640
    h = 480
    size=(w,h)
    screen = pygame.display.set_mode(size) 
    screen.blit(image,(0,0))
    pygame.display.flip()
    return


def save_image(image,filename):
    cv2.imwrite(filename,image)
    
def load_image(filename):
    #body = cv2.imread(filename,0)
    f = open(filename, "rb")
    body = f.read()
    f.close()
    return body
    
def transform_image(image):
    filename = "/tmp/emotion.jpg"
    save_image(image,filename)
    return load_image(filename)