# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 14:28:56 2018

@author: amine
"""

#emotion_api
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 21:14:57 2017

@author: Wall-e group
"""

#emotion.api
 
import http.client, urllib.request, urllib.parse, urllib.error
def get_emotion(body):
    
    headers = {
        # Request headers. Replace the placeholder key below with your subscription key.
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': 'Your key',
        
    }
    
    params = urllib.parse.urlencode({
    })
    try:
        # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
        #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the 
        #   URL below with "westcentralus".
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params,body, headers)
        response = conn.getresponse()
        data = response.read().decode("utf-8")
        conn.close()
        return data
    except Exception as e:
        print(e.args)
    
