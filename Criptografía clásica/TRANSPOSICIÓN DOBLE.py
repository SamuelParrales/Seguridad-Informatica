#Escuela Superior politecnica de chimborazo
#By: Samuel Parrales

import re

def transposicionSimple(texto):
    primerGrupo = ''
    segundoGrupo = ''

    for i in range(0,len(texto)):
        if((i+1)%2!=0):
            primerGrupo+=texto[i]
        else:
            segundoGrupo+=texto[i]
    
    return  (primerGrupo + segundoGrupo)

texto = "MAGNO TEMPLO, BASTION DE LA PATRIA MANANTIAL DE CULTURA Y SAPIENCIA, DE HUMANISMO, DE TECNICA Y CIENCIA DEL ESPIRITU ELIXIR VITAL"
textoLimpio = re.sub(r'\.|,|;|\s','',texto)
transpSimple = transposicionSimple(textoLimpio)
cripto = transposicionSimple(transpSimple)

print(cripto)
