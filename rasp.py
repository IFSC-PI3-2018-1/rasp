# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 17:23:04 2018

@author: pedrohames
"""

import base64
import requests
#import json
import color_figure_detector
import asyncio
import websockets

def start_server(self):
    colors = str(color_figure_detector.get_colors())
    r = requests.post('http://localhost:5000/postacor', data={'lista':colors})
    websockets.serve(_handle, 'localhost', 20181)
    
async def _handle(websocket, path):
    
    req = await websocket.recv()
    ##GET IMAGEM
    
    color_figure_detector.main('Image/testecores.jpg', req[1])
    
    with open("Image/testecores.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        
    
    payload = {'nID':req[0],'origem':'rasp','conteudo':encoded_string.decode('utf-8')}
    
    r = requests.post('http://localhost:5000/imagens_enviadas', json=payload)
#    print(r.status_code, r.reason)
    
    
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()   


