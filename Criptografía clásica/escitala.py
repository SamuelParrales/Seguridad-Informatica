from random import lognormvariate
import re
import math

def generarMatriz(filas):
    M =[]
    for i in range(filas):
        M.append([])
    return M

def crearEscilata(filas,texto):
    loops = len(texto)
    columnas = math.ceil(loops/filas)
    escilata = generarMatriz(filas)
    for i in range(0,filas):
        for j in range(0,columnas):
            pos = i*columnas + j
            if(pos>=loops):
                escilata[i].append('-')
                continue
            escilata[i].append(texto[pos])
    return escilata


def desenrrollarCinta(M):
    filas = len(M)
    columnas = len(M[0])
    cripto = ""
    for j in range(columnas):
        for i in range(filas):
            cripto +=M[i][j]
    return cripto

texto = "MAGNO TEMPLO, BASTION DE LA PATRIA MANANTIAL DE CULTURA Y SAPIENCIA, DE HUMANISMO, DE TECNICA Y CIENCIA DEL ESPIRITU ELIXIR VITAL"
textoLimpio = re.sub(r'\.|,|;|\s','',texto)

escilata = crearEscilata(5,textoLimpio)
loops = len(escilata)
for i in range (loops):
    print(escilata[i])

print(desenrrollarCinta(escilata))