#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 12:08:32 2023

@author: sofiaescobar
"""

import ControllerP0 as c




def verifyTodo():
    programa = str(print("Enter the robot program: "))
    syntaxis=c.verifyTodo(programa)
    
    if syntaxis==True:
        print('Syntaxis is correct')
    if syntaxis==False:
        print('Syntaxis has an error')
     
            
verifyTodo()