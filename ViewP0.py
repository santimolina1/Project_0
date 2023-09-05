#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 12:08:32 2023

@author: sofiaescobar
"""

import ControllerP0 as c
from pathlib import Path

print("Bienvenido, programa de verificación:")
print('Asegúrese de que el archivo esté en la carpeta.')
archivo = input("Por favor, introduzca el archivo.txt con el código a verificar: ")
p = Path(__file__).with_name(archivo)
print("Verificando su código...")
res = ""
if c.verifyTodo(p):
    res = 'Su código es correcto.'
else:
    res = 'Su código tiene errores.'
print(res)
