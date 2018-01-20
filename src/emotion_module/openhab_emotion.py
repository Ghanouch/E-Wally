# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 15:15:01 2018

@author: amine
"""

#openhab script to update text state
import openhab
#import datetime

from openhab import Item

base_url = 'http://localhost:8080/rest'


def set_openhab_emotion_text(emotion_result):
    emotion_text = openhab.get_item(base_url, 'emotion_item')
    emotion_text.state = emotion_result
def is_switch_on():
    switch_item = openhab.get_item(base_url, 'test_switch')
    if(switch_item.state=="ON"):
        return True
    return False
