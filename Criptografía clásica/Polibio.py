import re
import math
from typing import Text

def generarMatriz(): #Esta matriz no tiene la letra Q
    equAscci = 65 #Letra A
    M = []

    for i in range (5):
        M.append([])
        for j in range (5):
            letra = chr(equAscci)
            M[i].append(letra)
            equAscci+=1
            if(equAscci==81):  #Se ignora la letra Q
                equAscci+=1
    return M

def buscar(M, caracter):
    loops = len(M)
    for i in range(loops):
        try:
            j = M[i].index(caracter)
            return [i,j]
        except:
            continue
    

def polibio(texto,sustitucion):
    M = generarMatriz()
    loops = len(texto)    
    cripto = ""
   
    for i in range(loops):
        pos = buscar(M,texto[i])
        f = pos[0] #Filas 
        c = pos[1] #Columnas
        elemento = sustitucion[f] + sustitucion[c]
        cripto+=elemento
    return cripto

texto = "MAGNO TEMPLO, BASTION DE LA PATRIA MANANTIAL DE CULTURA Y SAPIENCIA, DE HUMANISMO, DE TECNICA Y CIENCIA DEL ESPIRITU ELIXIR VITAL"
textoLimpio = re.sub(r'\.|,|;|\s','',texto)

#sustitucion = ['A','B','C','D','E']
sustitucion = ['0','1','2','3','4']
print(polibio(textoLimpio,sustitucion))


