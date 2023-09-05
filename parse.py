import sys

commands1={'drop','get','grab','letGo'}
commands2={'leap','walk'}
commands3={'jump'}
commands4={'nop'}
commands5={'turn'}
commands6={'turnto'}
commands7={'defVar'}
commands8={'defProc'}
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


def convertirPrograma(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            linea = file.read()
            linea = linea.replace('\t', ' ').replace('\n', ' ').replace('(',' ( ').replace(')',' ) ').replace(',',' , ').replace('{',' { ').replace('}',' } ').replace(';',' ; ')
            comandos = linea.split()
            comandos2 = [elemento for elemento in comandos if elemento != '']
            return comandos2
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no fue encontrado.")
        return []




def changeCommand(programa):
    newCommands=[]
    for command in programa: 
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
        elif command in commands8:
            command='F'
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

def verifyVariableDefinition(programa,i):
    correct=True
    if programa[i+1] in caracteresEspeciales and programa[i+2]!='#':
        correct=False
                
    return correct

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
#Verifica las condiciones
def verifyO(programa,i):
    
    
    if programa[i+1]!='(' and programa[i+2]not in procesos  :
        return False
    
    posicionI=i+2
    posicionF=posicionFinalTotal(programa,posicionI)
    if posicionF==False:
        return False
    if programa[posicionF]!=")" :
        return False
    return True


#Verifica las condicionales
def verifyI(programa,i):
    
    if programa[i+1]not in condiciones and programa[i+2]!="(" :
        print("1")
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
    
    posicionI2=posicionF1+3
    posicionF2=posicionFinalTotal(programa,posicionI2)
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
    
   
def verifyR(programa,i):
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


#verdifica DefProc
def verifyF(programa,i):
    if programa[i+1] not in procesos and programa[i+2]!="(":
        return False
    return True


def verifyTodo(programa):
    programa1=convertirPrograma(programa)
    programa2=changeCommand(programa1)
    cont1=0
    cont2=0
    for i in range(0, len(programa2) - 1):
        print(programa2[i])
        # Verificamos las funciones
        if programa2[i] == 'S' and not verifyS(programa2, i):
            return False
        if programa2[i] == 'P' and not verifyP(programa2, i):
            return False
        if programa2[i] == 'J' and not verifyJ(programa2, i):
            return False
        if programa2[i] == 'N' and not verifyN(programa2, i):
            return False
        if programa2[i] == 'T' and not verifyT(programa2, i):
            return False
        if programa2[i] == 'H' and not verifyH(programa2, i):
            return False

        # Verificamos las condicionales
        if programa2[i] == 'I' and not verifyI(programa2, i):
            return False
        if programa2[i] == 'O' and not verifyO(programa2,i):
            return False
        if programa2[i] == 'W' and not verifyW(programa2,i) :
            return False
        if programa2[i]=='F' and not verifyF(programa2,i):
            return False
        if programa2[i]=='R' and not verifyR(programa2,i):   
            return False
        #Verificamos los corchetes
        if programa2[i]=="{":
            cont1+=1
        if programa2[i]=="}":
            cont2+=1
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
