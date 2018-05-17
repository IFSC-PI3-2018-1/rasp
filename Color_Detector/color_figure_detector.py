# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 15:47:13 2018

@author: marcos
"""

import cv2 
import numpy as np

def color_detector(color, image,nome):
    
    (_,contours,hierarchy)=cv2.findContours(color,cv2.cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate (contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)
            image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,0),2)
            cv2.putText(image,nome,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0))
    
    return image

#
#definindo o range do violeta
def color_violet(hsv):
    lower_violet = np.array([140,110,80],np.uint8)
    upper_violet = np.array([160,255,255],np.uint8)
    violet = cv2.inRange(hsv,lower_violet,upper_violet) 
    return violet

#definindo o range do roxo
def color_purple(hsv):
    lower_purple = np.array([120,110,80],np.uint8)
    upper_purple = np.array([139,255,255],np.uint8)
    purple = cv2.inRange(hsv,lower_purple,upper_purple)  
    return purple

#definindo o range da cor azul
def color_blue(hsv):
    lower_blue = np.array([90,109,20],np.uint8)
    upper_blue = np.array([118,255,255],np.uint8)
    blue=cv2.inRange(hsv,lower_blue,upper_blue)
    return blue

#definindo o range da cor verde
def color_green(hsv):
    lower_green = np.array([38,100,50],np.uint8)
    upper_green = np.array([70,255,255],np.uint8)
    green = cv2.inRange(hsv,lower_green,upper_green) 
    return green

#definindo o range da cor amarelo
def color_yellow(hsv):
    lower_yellow = np.array([20,160,200],np.uint8)
    upper_yellow = np.array([35,255,255],np.uint8)
    yellow=cv2.inRange(hsv,lower_yellow,upper_yellow)
    return yellow

#definindo o range da cor laranja
def color_orange(hsv):
    lower_orange = np.array([10,120,200],np.uint8)
    upper_orange = np.array([21,255,255],np.uint8)
    orange=cv2.inRange(hsv,lower_orange,upper_orange)
    return orange

#definindo o range da cor vermelho
def color_red(hsv):
    lower_red = np.array([0,150,125],np.uint8)
    upper_red = np.array([10,255,255],np.uint8)
    lower_red1 = np.array([176,180,125],np.uint8)
    upper_red1 = np.array([179,255,255],np.uint8)    
    red=cv2.inRange(hsv,lower_red,upper_red)
    red1=cv2.inRange(hsv,lower_red1,upper_red1)
    return red,red1

def color_black(hsv):
    lower_black = np.array([0,0,0],np.uint8)
    upper_black = np.array([255,255,0],np.uint8)
    black = cv2.inRange(hsv,lower_black,upper_black)   
    return black


#convertendo frame BGR para HSV      

datapath = "/home/marcos/Documentos/pi3/OpenCV_python/CarData/TrainImages"
frame = cv2.imread('images.jpg',cv2.IMREAD_UNCHANGED)
      
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
color = color_blue(hsv)
retorno=color_detector(color,frame,"azul")


        
cv2.imshow('Cor detectada', retorno)   
cv2.waitKey()
cv2.destroyAllWindows()
