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
procesos=['S','P','J','N','T','H']
variables={}
functions={}
pila_calls=[]
programa=input()
condiciones={"can","facing","not"}


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
        elif command=="if":
            command='I'
        elif command=="while":
            command='W'
        elif command in condiciones:
            command='O'
        elif command=="repeat":
            command='R'
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

def verifyP(programa,i):
    correct=True
    
    if programa[i+5]==')':
        if programa[i+1]!='(' and programa[i+2]!='#' and programa[i+3]!=',' and programa[i+4] not in directions and programa[i+4] not in orientations and programa[i+5]!=')':
            correct=False
    if programa[i+3]==')':
        if programa[i+1]!='(' and programa[i+2]!='#' and programa[i+3]!=')':
            correct= False
        
        
    return correct
            

def verifyS(programa,i):
    correct=True
    
    
    if programa[i+1]!='(' and programa[i+2]!='#' and programa[i+3]!=')':
        correct= False
    return correct

def verifyJ(programa,i):
    correct=True
    
    
    if programa[i+1]!='(' and programa[i+2]!='#' and programa[i+3]!=',' and programa[i+4]!='#' and programa[i+5]!=')':
        correct=False
    return correct

def verifyN(programa,i):
    correct=True
    
     
    if programa[i+1]!='(' and programa[i+2]!=')':
        correct= False
    return correct

def verifyT(programa,i):
    correct=True
    
    
    if programa[i+1]!='(' and programa[i+2] not in directions and programa[i+3]!=')':
        correct=False
    return correct

def verifyH(programa,i):
    
    correct=True
    
    
    if programa[i+1]!="O" and programa[i+2] not in orientations and programa[i+3]!=')':
        correct=False
    return correct

def verifyI(programa,i):
    
    if programa[i+1]not in condiciones and programa[i+2]!="(" :
        return False
    
    posicionI=i+3
    posicionF=posicionFinalTotal(programa,posicionI)
    if posicionF==False:
        return False
    
    if programa[posicionF]!=")" and programa[posicionF+1]!="{" and programa[posicionF+2] not in procesos :
        return False
    
    posicionI1=posicionF+2
    posicionF1=posicionFinalTotal(programa,posicionI1)
    while programa[posicionF1]==";":
        posicionI1=posicionF1+1
        posicionF1=posicionFinalTotal(programa,posicionI1)
        if posicionF1==False:
            return False
    if programa[posicionF1]!="}" and programa[posicionF1+1]!="else" and programa[posicionF1+2]=="{" and programa[posicionF1+3] not in procesos:
        return False
    
    posicionF2=posicionF1+3
    posicionI2=posicionFinalTotal(programa,posicionF2)
    while programa[posicionI2]==";":
        posicionI2=posicionF2+1
        posicionF2=posicionFinalTotal(programa,posicionI2)
        if posicionF2==False:
            return False
    if programa[posicionF2]!="}":
        return False
    
    return True


def verifyW(programa,i):
    
    if programa[i+1]not in condiciones and programa[i+2]!="(" :
        return False
    
    posicionI=i+3
    posicionF=posicionFinalTotal(programa,posicionI)
    if posicionF==False:
        return False
    
    if programa[posicionF]!=")" and programa[posicionF+1]!="{" and programa[posicionF+2] not in procesos :
        return False
    
    posicionI1=posicionF+2
    posicionF1=posicionFinalTotal(programa,posicionI1)
    while programa[posicionF1]==";":
        posicionI1=posicionF1+1
        posicionF1=posicionFinalTotal(programa,posicionI1)
        if posicionF1==False:
            return False
    if programa[posicionF1]!="}":
        return False
    
    return True
    
   
def verifyO(programa,i):
    if programa[i+1] !="#" and programa[i+2]!="times" and programa[i+3]!="{" and programa[i+4] not in procesos:
        return False
    
    posicionO=i+4
    posicionF=posicionFinalTotal(programa,posicionO)
    while programa[posicionF]==";":
        posicionO=posicionF+1
        posicionF=posicionFinalTotal(programa,posicionO)
        if posicionF==False:
            return False
    if programa[posicionF]!="}":
        return False
    return True

    



def verifyTodo(programa):
    for i in range(0, len(programa) - 1):
        # Verificamos las funciones
        if programa[i] == 'S' and not verifyS(programa, i):
            return False
        if programa[i] == 'P' and not verifyP(programa, i):
            return False
        if programa[i] == 'J' and not verifyJ(programa, i):
            return False
        if programa[i] == 'N' and not verifyN(programa, i):
            return False
        if programa[i] == 'T' and not verifyT(programa, i):
            return False
        if programa[i] == 'H' and not verifyH(programa, i):
            return False

        # Verificamos las condicionales
        if programa[i] == 'I' and not verifyI(programa, i):
            return False
        if programa[i] == 'O' and not verifyO(programa,i):
            return False
        if programa[i] == 'W' and not verifyW(programa,i) :
            return False

    return True

def posicionFinalS(programa,i):
    return i+4
def posicionFinalP(programa,i):
    if programa[i+5]==')':
        return i+6
    elif programa[i+3]==')':
        return i+4
def posicionFinalJ(programa,i):
    return i+6
def posicionFinalN(programa,i):
    return i+3
def posicionFinalT(programa,i):
    return i+4
def posicionFinalH(programa,i):
    return i+4    

def posicionFinalTotal(programa,i):
    if programa[i]=='S':
        return posicionFinalS(programa,i)
    elif programa[i]=='P':
        return posicionFinalP(programa,i)
    elif programa[i]=='J':
        return posicionFinalJ(programa,i)
    elif programa[i]=='N':
        return posicionFinalN(programa,i)
    elif programa[i]=='T':
        return posicionFinalT(programa,i)
    elif programa[i]=='H':
        return posicionFinalH(programa,i)
    else:
        return False