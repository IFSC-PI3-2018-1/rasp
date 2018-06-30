# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 17:23:04 2018

@author: pedrohames
"""

import base64
import requests
import color_figure_detector
import zmq
import wget
import time

#FPGA = 'https://wiki.sj.ifsc.edu.br/wiki/images/3/3f/FotoAntena-EngTelecom.jpg'
FPGA = 'http://www.imagenspng.com.br/wp-content/uploads/2015/02/super-mario-mario-01.png'
WebService = 'http://localhost:5000'

# ANTENA IFSC
#https://wiki.sj.ifsc.edu.br/wiki/images/3/3f/FotoAntena-EngTelecom.jpg
def start_rasp():
    colors = str(color_figure_detector.get_colors())
    r = requests.post(WebService + '/post_cor', json={'lista':colors})
    if(r):
        print('Cores disponíveis enviadas ao servidor')
    port = "20181"
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect ("tcp://localhost:%s" % port)
    return socket

def getImage(url, requestId):
    path = '/tmp/'+ requestId + '.png'
    wget.download(url, path)
    return path

def imageProcessing(path,cor):
    lcor = []
    lcor.append(cor)
    color_figure_detector.main(path,lcor)
    
def imageToBase64(path):
    with open(path, "rb") as image_file:
        Ibase64 = base64.b64encode(image_file.read())
        return Ibase64
    
def sendImage(imagem,requestId):
    print('============================================')
    print(type(imagem))
    print(len(imagem))
    r = requests.post(WebService + '/enviar_imagem', json={'requestId':requestId,
                                                           'origem':'rasp',
                                                           'imagem': imagem,
                                                           'timestamp': str(time.time())})
    if(r):
        return True
    else:
        return False

if __name__ == "__main__":
    print('RASP INICIADA')
    socket = start_rasp()
    while(True):
        topic = 'requeststorasp'
        socket.setsockopt_string(zmq.SUBSCRIBE, topic)
        string = socket.recv()
        print('============= REQUISICAO RECEBIDA ===============')
        print(string)
        cor, requestId = string.split()[-2:]
        cor = cor.decode()
        requestId = requestId.decode()
        print(cor,requestId)
        path = getImage(FPGA, requestId)
        imageProcessing(path, cor)
        encodedImage = imageToBase64(path)
        if(sendImage(encodedImage, requestId)):
            print('Sucesso na requisição: ' + requestId)
        else:
            print('Falha ao atender requisição: ' + requestId)        
    
    
    
