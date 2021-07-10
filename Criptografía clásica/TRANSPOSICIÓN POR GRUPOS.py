#Escuela Superior politecnica de chimborazo
#By: Samuel Parrales


import re

def redondeoGrupo(grupo,longitud):
    ultimoCrt = 88
    loops = longitud - len(grupo)
    for i in range(0,loops):
        grupo+= chr(ultimoCrt)
        if(ultimoCrt<90):
            ultimoCrt+=1
        else:
            ultimoCrt = 65
    return grupo


def reemplazarPos(grupo,clave):
    grupo = redondeoGrupo(grupo,len(clave))
    loops = len(grupo)
    cripto =''
    for i in range(0,loops):
        pos = int(clave[i]) - 1
        cripto += grupo[pos] 

    return cripto

def transposicion(texto, clave):
    salto = len(clave)
    limiteGroup = salto
    inicioGroup =0
    loops = len(texto)
    cripto = ''
    for i in range(0,loops,salto):
        grupo = texto[inicioGroup:limiteGroup]
        cripto += reemplazarPos(grupo,clave)
        inicioGroup = limiteGroup
        limiteGroup += salto 
    return cripto
    
texto = "MAGNO TEMPLO, BASTION DE LA PATRIA MANANTIAL DE CULTURA Y SAPIENCIA, DE HUMANISMO, DE TECNICA Y CIENCIA DEL ESPIRITU ELIXIR VITAL"
textoLimpio = re.sub(r'\.|,|;|\s','',texto)
print(transposicion(textoLimpio,'341265'))

