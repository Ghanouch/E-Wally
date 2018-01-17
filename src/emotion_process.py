# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 15:03:32 2018

@author: amine
"""

#result process
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 11:37:38 2017

@author: Wall-e group
"""

#process result 
import json
from collections import namedtuple
def process_result(result):
    x = json.loads(result, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    if(len(x)==0 and x[0]):
        d = "Could not process the image"
    else : 
        #display the result
        happy_score , neutral_score ,sad_score= x[0].scores.happiness  , x[0].scores.neutral,x[0].scores.sadness
        fear_score ,anger_score,surprise_score= x[0].scores.fear,x[0].scores.anger,x[0].scores.surprise
        disg_score = x[0].scores.disgust
        contempt_score = x[0].scores.contempt
        res  = {'Happy':happy_score,
            'Sad': sad_score,
            'Neutral':neutral_score,
            'Surprised':surprise_score,
            'Afraid':fear_score,
            'Disgusted':disg_score,
            'Angry':anger_score,
            'Contempt':contempt_score
            }
        d1 =  max(res.values())
        d = max(res, key=res.get)
        if(d=='Neutral') :
            res_2  = {'Happy':happy_score,
            'Sad': sad_score,
            'Surprised':surprise_score,
            'Afraid':fear_score,
            'Disgusted':disg_score,
            'Angry':anger_score,
            'Contempt':contempt_score
            }
            
            d2 = max(res_2.values())
            #print((d1,d2))
            if(d1-d2 <= 0.30):
                d=max(res_2, key=res.get)
    return d
    