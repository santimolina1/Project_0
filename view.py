#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 12:08:32 2023

@author: sofiaescobar
"""

import model as verify
from pathlib import Path

def programInput():
        program_path = input("Enter the path to the robot program file: ")
        return program_path

def show_result(program):
    programa= programInput()
    
    if verify.verificarSyntaxis(programa):
        print('Syntaxis is correct')
    else:
        print('Syntaxis has an error')
     
            
