# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 13:28:35 2018

@author: amine
"""

#utils
import time
def get_curent_time():
    return int(round(time.time() * 1000))
    
def wait_for(time):
    current_milli_time_1 = get_curent_time()
    while(get_curent_time()-current_milli_time_1 < time):
            pass
def is_time_passed(current_milli_time,wait):
    while(get_curent_time()-current_milli_time < wait):
            pass
    return True
    