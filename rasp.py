# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 17:23:04 2018

@author: pedrohames
"""

import base64
import requests
import json
import color_figure_detector


def __handle(self):
    ##Processamento CV2
    
    with open("Image/testecores.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        
    print(type(encoded_string))
    
    payload = {'nID':'3','id_facebook':'12345','origem':'rasp','conteudo':encoded_string.decode('utf-8')}
    print(type(payload))
    
    r = requests.post('http://localhost:5000/imagens_enviadas', json=payload)
    print(r.status_code, r.reason)


