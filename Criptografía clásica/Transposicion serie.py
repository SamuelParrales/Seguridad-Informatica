import re
texto = "MAGNO TEMPLO, BASTION DE LA PATRIA MANANTIAL DE CULTURA Y SAPIENCIA, DE HUMANISMO, DE TECNICA Y CIENCIA DEL ESPIRITU ELIXIR VITAL"

textoLimpio = re.sub(r'\.|,|;|\s','',texto)

loops = len(textoLimpio)
MS1 = '' #Multiplo de 5
MS2 = '' #Multiplo de 3
MS3 = '' #Impar
MS4 = '' #PAR
for i in range(0,loops):
    pos = i+1
    if(pos%5==0):
        MS1+=textoLimpio[i]
        continue
    if(pos%3==0):
        MS2+=textoLimpio[i]
        continue

    if(pos%2!=0): #Es impar
        MS3 += textoLimpio[i]
        continue

    MS4 +=textoLimpio[i] #Es par

print(MS1)
print(MS2)
print(MS3)
print(MS4)

