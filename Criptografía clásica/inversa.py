import re
texto = "Magno templo, bastión de la patria manantial de cultura y sapiencia, de humanismo, de técnica y ciencia del espíritu elixir vital"

textoLimpio = re.sub(r'\.|,|;|\s','',texto)

print(textoLimpio)

cripto = ''.join(reversed(textoLimpio))
print(cripto)
