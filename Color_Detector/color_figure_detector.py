# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 15:47:13 2018
@author: marcos
"""

import cv2 
import numpy as np

def color_detector(color, image,nome):

    	
    if nome == "azul": 
        rectangle_color = (255,0,0)
    elif nome == "amarelo": 
        rectangle_color = (0,255,255)
    elif nome == "vermelho":
        rectangle_color = (0,0,255)
    elif nome == "preto":
        rectangle_color = (0,0,0)
    elif nome == "alaranjado": 
        rectangle_color = (3,163,255)
    elif nome == "roxo": 
        rectangle_color = (200,0,87)
    elif nome == "violeta": 
        rectangle_color = (160,0,125)
    elif nome == "verde": 
        rectangle_color = (0,255,0)
    elif nome == "rosa": 
        rectangle_color = (130,0,255)
    else: 
        rectangle_color = (0,0,0)
    
    (_,contours,hierarchy)=cv2.findContours(color,cv2.cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate (contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)
            image = cv2.rectangle(image,(x,y),(x+w,y+h),rectangle_color,2)
            cv2.putText(image,nome,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,rectangle_color)
    
    return image

#
#definindo o range do rosa
def color_pink(hsv):
    lower_pink = np.array([161,110,80],np.uint8)
    upper_pink = np.array([167,255,255],np.uint8)
    pink = cv2.inRange(hsv,lower_pink,upper_pink) 
    return pink


#definindo o range do violeta
def color_violet(hsv):
    lower_violet = np.array([140,110,80],np.uint8)
    upper_violet = np.array([160,255,255],np.uint8)
    violet = cv2.inRange(hsv,lower_violet,upper_violet) 
    return violet

#definindo o range do roxo
def color_purple(hsv):
    lower_purple = np.array([125,110,80],np.uint8)
    upper_purple = np.array([139,255,255],np.uint8)
    purple = cv2.inRange(hsv,lower_purple,upper_purple)  
    return purple

#definindo o range da cor azul
def color_blue(hsv):
    lower_blue = np.array([90,109,50],np.uint8)
    upper_blue = np.array([120,255,255],np.uint8)
    blue=cv2.inRange(hsv,lower_blue,upper_blue)
    return blue

#definindo o range da cor verde
def color_green(hsv):
    lower_green = np.array([38,120,50],np.uint8)
    upper_green = np.array([80,255,255],np.uint8)
    green = cv2.inRange(hsv,lower_green,upper_green) 
    return green

#definindo o range da cor amarelo
def color_yellow(hsv):
    lower_yellow = np.array([20,110,200],np.uint8)
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


#Retorna as cores detectáveis
def get_colors():
    
    def_colors = ["azul","amarelo", "vermelho", "preto", "laranja","roxo", "violeta", "verde", "rosa"]
    return def_colors

def processing(color, hsv):
    
    if color == "azul":
        range_color = color_blue(hsv)
        
    elif color == "amarelo": 
        range_color = color_yellow(hsv)
        
    elif color == "vermelho":
        range_color = color_red(hsv)
        
    elif color == "preto":
        range_color = color_black(hsv)
        
    elif color == "laranja": 
        range_color = color_orange(hsv)
        
    elif color == "roxo": 
        range_color = color_purple(hsv)
        
    elif color == "violeta": 
        range_color = color_violet(hsv)
        
    elif color == "verde": 
        range_color = color_green(hsv)
        
    elif color == "rosa": 
        range_color = color_pink(hsv)
        
    else:  range_color = 1
           
    return range_color



def main(datapath,color):  

    frame = cv2.imread(datapath,cv2.IMREAD_UNCHANGED) 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #conversao para hsv

    processing(color,hsv)
    num = len(color)
    
    for x in range(0,num):
        range_color = processing(color[x],hsv)
        print color[x]
        if range == 1:
            print "Erro"
        else:
            retorno=color_detector(range_color,frame,color[x])
            
    cv2.imwrite('MyPic.jpg', retorno)     
            
    return retorno

datapath = "images.jpg" #localização da imagem
color = ["azul", "verde"] # sequ   
retorno = main(datapath,color)
        
cv2.imshow('Cor detectada', retorno)   
cv2.waitKey()
cv2.destroyAllWindows()
l