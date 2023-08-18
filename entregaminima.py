import re
numLinea = 1
ans = 0
#Definicion de funciones
def cupon(x, y=None):
    #hacer algo
    if y is None:
        z = x * 0.2
        return (z)
    else:
        z = (y*x)/100
        z = z//1
        return (z)

def sumar(a,b):
    return (a + b)

def restar(a,b):
    z = a - b
    if z < 0:
        return (0)
    else:
        return (z)
    

def multiplicar(a,b):
    return (a * b)

def divisionEntera(a,b):
    if b != 0:
        return (a//b)
    else:
        return("no se puede dividir por 0")


def verificarLinea(linea):
    global ans
    if re.search("ANS", linea): #chequea si hay algun ANS en la linea para intercambiarlo por su valor
        print(linea)
        linea = re.sub(r"ANS", str(ans), linea)
        #print(linea)
    sintaxisCorrecta = r"^\d+(\s*([-+*]|\s*\/\/\s*)\s*\d+)*$"
    print(linea)
    if re.match(sintaxisCorrecta, linea.strip()): #verifica que la sintaxis este correcta
        if re.search(r"//\s*0", linea):           # verifica que no existe alguna division por 0
            print("no se puede dividir por 0")
            return (False)
        else:    
            print("la sintaxis esta correcta")
            return (True)
    
        #hacer algo para escribir en las lineas de desarrollo, en cada linea si fue "error" o "sin resolver"
    elif re.match("\n", linea):
        print("bien")
    else:
        print("error en la sintaxis")
        return (False)


def procesarSentencia(sentencia):
    global ans
    global numLinea
    print("procesando")
    if re.search("ANS", sentencia): #chequea si hay algun ANS en la linea para intercambiarlo por su valor
        #print("ANS = ", ans)
        sentencia = re.sub("ANS", str(ans), sentencia)
    elementos = re.findall(r"\d+|[+-]", sentencia)
    #print(elementos)
    resultado = 0
    operacion = ""
    for i in elementos: 
        operacion += i
        print(operacion)
        if re.match(r"\d+([+-])\d+", operacion): #si la operacion esta correcta busca para resolverla
            nums = re.findall(r"\d+", operacion)
            a = int(nums[0])
            b = int(nums[1])
            if re.search(r"-", operacion): 
                resultado = restar(a,b)
            elif re.search(r"\+", operacion):
                resultado = sumar(a,b)
            operacion = str(resultado)
            resultado = 0
    print("el resultado de la linea " + str(numLinea) + " es: " + operacion + "\n")
    if re.match(r"\d+",operacion):
        ans = int(operacion)
    print(operacion)
    numLinea += 1
    return (operacion)





    

     

#Main
with open("problemaspro.txt", "r") as problemas: #Abre el archivo.txt donde estan los problemas
    listaProblemas = problemas.readlines() # Entrega una lista con los problemas del archivo.txt
    #print(listaProblemas) # ['200000 - 5000 + 2 + 1320 - 10 + 3\n', 'ANS - 4500 + 300 + 5 + 25 - 7\n', 'ANS - 15\n', '\n']

    for sentencia in listaProblemas: #recorre la lista de problemas
        if verificarLinea(sentencia): #revisa si la linea esta bien escrita (con sintaxis correcta)
            procesarSentencia(sentencia)
        elif sentencia == "\n":
            print("Se termino este problema. Pasemos al siguiente...")
            ans = 0
            numLinea = 1
        else:
            print("no se puede resolver")
            print(sentencia)


'''elif re.match(r"",linea):
        print("Se termino este problema. Pasemos al siguiente...")
        ans = 0
        numLinea = 1
        return(True)'''

'''with open("desarrollo.txt", "w") as desarrollo:
    desarrollo.write("desarrollo")
    print(desarrollo)'''