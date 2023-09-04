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


def verificarSyntaxis(programa):
    
    programaConvertido=convertirPrograma(programa)
    
    insideFunction=False 
    for comando in programaConvertido:
        if not comandoValido(comando):
            print(f"Syntax Error: Invalid command: {comando}")
            return False
        
    for comando in programaConvertido:
        if not direccionValida(comando):
            print(f"Syntax Error: Invalid command: {comando}")
            return False
    for nombre in programaConvertido:
        if not funcionDefinida(nombre):
            print(f"Syntax Error: Invalid command: {comando}")
            return False
        
    return True
