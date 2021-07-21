#65:A - 90:Z

import re
def desplazamiento(caracter,clave):
    salto = ord(clave)-64
    numberAscii = ord(caracter)
    numberAscii += salto
    if(numberAscii>90):
        numberAscii-=26
    return [chr(numberAscii),numberAscii-64]

def sustitucionDesplazamiento(texto, clave):
    longitudClave = len(clave)
    loops = len(texto)
    repNum = []
    cripto = []
    for i in range(loops):
        k = i%longitudClave
        par = desplazamiento(texto[i],clave[k])
        cripto.append(par[0])
        repNum.append(par[1])

    return [cripto,repNum]


texto = "MAGNO TEMPLO, BASTION DE LA PATRIA MANANTIAL DE CULTURA Y SAPIENCIA, DE HUMANISMO, DE TECNICA Y CIENCIA DEL ESPIRITU ELIXIR VITAL"
textoLimpio = re.sub(r'\.|,|;|\s','',texto)

clave ='BALCF'

textoNumber =[]
for i in range(len(textoLimpio)):
    textoNumber.append(ord(textoLimpio[i])-64)

print(textoLimpio)
print("")
print(textoNumber)
print("")
cifrado = sustitucionDesplazamiento(textoLimpio,clave)
print(cifrado[0])
print("")
print(cifrado[1])



