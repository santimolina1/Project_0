import sys

commands= {'M','R','C','B','c','b','P'}
directions={'north', 'east', 'west','south'}
symbols=set([":", ",", ";", "[", "]"])
orientations={'right','left','front','back'}

variables={}
functions={}
pila_calls=[]


def convertirPrograma(programa):
    programa = programa.replace('\t', ' ').replace('\n', ' ')
    comandos = programa.split()
    return [comandos.lower() for comando in comandos]


def comandoValido(comando):
    return comando in commands

def direccionValida(comando):
    return comando in directions

def funcionDefinida(nombre):
    return nombre in functions
