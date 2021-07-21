import re
import random
def redondearBin(binario):
    longitud = len(binario)
    loops = 8-longitud
    newBin =""
    for i in range(loops):
        newBin+='0'
    newBin += binario
    return newBin

def VERNAM(texto,clave):
    loops = len(texto)
    cifrado = []
    numersAscii = []
    numersBin = []
    claveBin = []
    for i in range(loops):
        
        numAscii= ord(texto[i])
        numersAscii.append(numAscii)
        numBin = format(numAscii,'b')
        numersBin.append(redondearBin(numBin))

        numAsciiClave = ord(clave[i])
        kBin = format(numAsciiClave,'b')
        claveBin.append(redondearBin(kBin))

        cripto = numAscii^numAsciiClave
        cripBin = format(cripto,'b')
        cifrado.append(redondearBin(cripBin))
    
    return [numersAscii,numersBin,claveBin,cifrado]
        
def caracterAleatorio():
    numberAscii = random.randint(33,159)
    return chr(numberAscii)

def generarCadena(longitud):
    cadena = ""
    for i in range(longitud):
        cadena += caracterAleatorio()
    return cadena
    
texto = "MAGNO TEMPLO, BASTION DE LA PATRIA MANANTIAL DE CULTURA Y SAPIENCIA, DE HUMANISMO, DE TECNICA Y CIENCIA DEL ESPIRITU ELIXIR VITAL"
textoLimpio = re.sub(r'\.|,|;|\s','',texto)

clave = generarCadena(len(textoLimpio))


L= VERNAM(textoLimpio,clave)
print(L[0])
print(L[1])
print("")
print(L[2])
print("")
print(L[3])