#Escuela Superior politecnica de chimborazo
#By: Samuel Parrales
import re
texto = "Magno templo, bastion de la patria manantial de cultura y sapiencia, de humanismo, de tecnica y ciencia del espiritu elixir vital"
textoLimpio = re.sub(r'\.|,|;|\s','',texto)

primerGrupo = ''
segundoGrupo = ''

for i in range(0,len(textoLimpio)):
    if((i+1)%2!=0):
        primerGrupo+=textoLimpio[i]
    else:
        segundoGrupo+=textoLimpio[i]

cripto = primerGrupo + segundoGrupo

print(cripto)