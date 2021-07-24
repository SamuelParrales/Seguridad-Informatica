#Escuela Superior Politécnica de Chimborazo
#By: Samuel Parrales
#65:A - 90:Z
import re
import random
def generacionMatriz():
    inicio = 65
    matriz = []
    for i in range(0,26):
        matriz.append([])
        for j in range(0,26):
            caracter = inicio + j
            if(caracter>90):
                caracter-= 26
            matriz[i].append(chr(caracter))
        inicio+=1
    return matriz


def vigenere(texto,clave):
    loops = len(texto)
    lenClave = len(clave)
    M= generacionMatriz()
    cifrado = ""
    for i in range(loops):
        k = i%lenClave
        C= ord(texto[i])-65
        F= ord(clave[k])-65
        cifrado += M[F][C]
    return cifrado



texto = "MAGNO TEMPLO, BASTION DE LA PATRIA MANANTIAL DE CULTURA Y SAPIENCIA, DE HUMANISMO, DE TECNICA Y CIENCIA DEL ESPIRITU ELIXIR VITAL"
textoLimpio = re.sub(r'\.|,|;|\s','',texto)
clave ="XZIQA"

print(vigenere(textoLimpio,clave))


 



