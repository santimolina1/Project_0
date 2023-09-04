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

def verificarSintaxis(programa):
    programaConvertido = convertirPrograma(programa)
    insideFunction = False

    for i, comando in enumerate(programaConvertido):
        if not comandoValido(comando):
            if comando.startswith("J(") and comando.endswith(")"):
                
                jump_params = comando[2:-1].split(',')
                if len(jump_params) == 2 and jump_params[0].isdigit() and jump_params[1].isdigit():
                    continue  
            elif comando.startswith("G(") and comando.endswith(")"):
                
                go_to_params = comando[2:-1].split(',')
                if len(go_to_params) == 2 and go_to_params[0].isdigit() and go_to_params[1].isdigit():
                    continue  

            print(f"Syntax Error at position {i + 1}: Invalid command: {comando}")
            return False

        if not direccionValida(comando):
            print(f"Syntax Error at position {i + 1}: Invalid command: {comando}")
            return False

        if insideFunction:
            if comando == '}':
                insideFunction = False
            continue

        if comando == 'defvar':
            
            if i + 2 < len(programaConvertido) and programaConvertido[i + 1] not in variables:
                variables[programaConvertido[i + 1]] = programaConvertido[i + 2]
            else:
                print(f"Syntax Error at position {i + 1}: Invalid variable definition")
                return False
        elif comando == 'defproc':
            
            if i + 2 < len(programaConvertido) and programaConvertido[i + 1] not in functions:
                function_name = programaConvertido[i + 1]
                i += 2
                if i < len(programaConvertido) and programaConvertido[i] == '(':
                    i += 1
                    parameters = []
                    while i < len(programaConvertido) and programaConvertido[i] != ')':
                        if programaConvertido[i] != ',':
                            parameters.append(programaConvertido[i])
                        i += 1
                    if i < len(programaConvertido) and programaConvertido[i] == ')':
                        functions[function_name] = parameters
                    else:
                        print(f"Syntax Error at position {i + 1}: Invalid function parameter list")
                        return False
                else:
                    print(f"Syntax Error at position {i + 1}: Missing function parameter list")
                    return False
            else:
                print(f"Syntax Error at position {i + 1}: Invalid function definition")
                return False
        elif comando == '{':
            insideFunction = True
            continue
    return True
