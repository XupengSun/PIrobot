#!/usr/bin/python3
#coding=utf8
import sys

servo1 = 1051 
servo2 = 1365 

centerx = 286 
###############################################
#颜色的字典
color_range = {
'red': [(0, 147, 0), (255, 255, 166)], 
'green': [(0, 0, 0), (255, 106, 255)], 
'blue': [(0, 0, 0), (255, 255, 120)],
'black': [(0, 0, 0), (56, 255, 255)], 
'white': [(193, 0, 0), (255, 250, 255)], 
              }

#backup
'''
color_range = {
'red': [(0, 147, 0), (255, 255, 166)], 
'green': [(0, 0, 0), (255, 106, 255)], 
'blue': [(0, 0, 0), (255, 255, 120)],
'black': [(0, 0, 0), (55, 255, 255)], 
'white': [(193, 0, 0), (255, 250, 255)], 
              }
'''