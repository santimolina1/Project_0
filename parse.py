import sys

commands1={'drop','get','grab','letGo'}
commands2={'leap','walk'}
commands3={'jump'}
commands4={'nop'}
commands5={'turn'}
commands6={'turnto'}
commands7={'defVar'}
values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
directions={'north', 'east', 'west','south'}
symbols=set([":", ",", ";", "[", "]"])
orientations={'right','left','front','back'}

variables={}
functions={}
pila_calls=[]
programa=input()



def convertirPrograma(programa):
    programa = programa.replace('\t', ' ').replace('\n', ' ').replace('(',' ( ').replace(')',' ) ').replace(',',' , ').replace('{',' { ').replace('}',' } ').replace(';',' ; ')
    comandos = programa.split(' ')
    comandos2 = [elemento for elemento in comandos if elemento != '']
    return comandos2




def changeCommand(programa):
    nuevoPrograma=convertirPrograma(programa)
    newCommands=[]
    for command in nuevoPrograma: 
        if command in commands1:
            command='S'
        if command in commands2:
            command='P'
        if command in commands3:
            command='J'
        if command in commands4:
            command='N'
        if command in commands5:
            command='T'
        if command in commands6:
            command='H'
        if command in commands7:
            command='B'
        newCommands.append(command)
    return newCommands
