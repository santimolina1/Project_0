import sys

commands1={'drop','get','grab','letGo'}
commands2={'leap','walk'}
commands3={'jump'}
commands4={'nop'}
commands5={'turn'}
commands6={'turnto'}
commands7={'defVar'}
directions={'north', 'east', 'west','south'}
symbols=set([":", ",", ";", "[", "]"])
orientations={'right','left','front','back'}
caracteresEspeciales=['S', 'P','J','N','T','H','B','#',';','}','{','(',')',',',':']

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
        elif command in commands2:
            command='P'
        elif command in commands3:
            command='J'
        elif command in commands4:
            command='N'
        elif command in commands5:
            command='T'
        elif command in commands6:
            command='H'
        elif command in commands7:
            command='B'
        elif command.isnumeric():
            command = '#'
        newCommands.append(command)
    return newCommands

def verifyVariableDefinition(programa):
    programa1=changeCommand(programa)
    correct=True
    
    for i in range(0,len(programa1)-1):
        if programa1[i]=='B':
            
            if programa1[i+1] in caracteresEspeciales and programa[i+2]!='#':
                correct=False
                
    return correct

programa=changeCommand(programa)

def verifyP(programa):
    correct=True
    for i in range(0,len(programa)-1):
        if programa[i]=='P' and programa[i+5]==')':
            if programa[i+1]!='(' or programa[i+2]!='#' or programa[i+3]!=',' or programa[i+4] not in directions or programa[i+4] not in orientations or programa[i+5]!=')':
                correct=False
        if programa[i]=='P' and programa[i+3]==')':
            if programa[i+1]!='(' or programa[i+2]!='#' or programa[i+3]!=')':
                correct= False
        
        
    return correct
            

def verifyS(programa):
    correct=True
    for i in range(0,len(programa)-1):
        if programa[i]=='S':
            if programa[i+1]!='(' or programa[i+2]!='#' or programa[i+3]!=')':
                correct= False
    return correct

def verifyJ(programa):
    correct=True
    for i in range(0,len(programa)-1):
        if programa[i]=='J':
            if programa[i+1]!='(' or programa[i+2]!='#' or programa[i+3]!=',' or programa[i+4]!='#' or programa[i+5]!=')':
                correct=False
    return correct

def verifyN(programa):
    correct=True
    for i in range(0,len(programa)-1):
        if programa[i]=='N':
            if programa[i+1]!='(' or programa[i+3]!=')':
                correct= False
    return correct

def verifyT(programa):
    correct=True
    for i in range(0,len(programa)-1):
        if programa[i]=='T':
            if programa[i+1]!='(' or programa[i+2] not in directions or programa[i+3]!=')':
                correct=False
    return correct

def verifyH(programa):
    
    correct=True
    for i in range(0,len(programa)-1):
        if programa[i]=='H':
            if programa[i+1]!='(' or programa[i+2] not in orientations or programa[i+3]!=')':
                correct=False
    return correct
