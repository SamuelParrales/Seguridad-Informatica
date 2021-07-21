
import copy
import math
import random
import re

def imprimirMatriz(M):
    loops = len(M)
    for i in range(loops):
        print(M[i])

def caracterAleatorio():
    numberAscii = random.randint(65,90)
    return chr(numberAscii)
def getCriptograma(M):
    dimension = len(M)
    criptograma=""
    for i in range(0,dimension):
        for j in range(0,dimension):
            criptograma+= str(M[j][i])
    return criptograma


def encontrar(par,arreglo):
    if(par in arreglo):
        return True
    return False

def rotarRigth(MR): #Metodo que rotará la matriz
    fila =[]
    M =[]
    for i in range(0,6):
        for j in range(5,-1,-1):
            fila.append(MR[j][i])
        M.append(fila)
        fila = []
    return M
            

def generarMatriz(MR,texto,con):
    M= copy.deepcopy(MR)
    for i in range(5,-1,-1):
        for j in range(0,6):
            if(M[j][i]):
                if(con<len(texto)):  
                    M[j][i] = texto[con]
                    con +=1
                    continue
                #M[j][i] = "-"
                M[j][i] = caracterAleatorio()  
            else:
                M[j][i] = caracterAleatorio() 
                #M[j][i] = "-"
    return M

def mascaraRotativa(posiciones,texto): #Solo para matriz de 6x6
    matrizR = [[],[],[],[],[],[]]
    cantRotacion = math.ceil(len(texto)/len(posiciones))
    
    for i in range(0,6): #Generacion de la matriz a ser rotada
        for j in range(0,6):
            matrizR[i].append(encontrar([j,i],espacioBlanco))
    print(1)
    M = generarMatriz(matrizR,texto,0)
    imprimirMatriz(M)
    crifrado = getCriptograma(M)
  
    for i in range(1,cantRotacion):
        print(i+1)
        matrizR = rotarRigth(matrizR)
        M=generarMatriz(matrizR,texto,len(posiciones)*i)
        imprimirMatriz(M)
        crifrado+= getCriptograma(M)
       
    return crifrado

texto = "MAGNO TEMPLO, BASTION DE LA PATRIA MANANTIAL DE CULTURA Y SAPIENCIA, DE HUMANISMO, DE TECNICA Y CIENCIA DEL ESPIRITU ELIXIR VITAL"
textoLimpio = re.sub(r'\.|,|;|\s','',texto)

espacioBlanco = [[0,0],[0,4],[1,0],[1,2],[2,5],[3,4],[4,1],[1,5],[2,1],[2,4],[3,2],[4,4],[5,1],[5,3],[5,5]]

cifrado = mascaraRotativa(espacioBlanco,textoLimpio)

print(cifrado)




