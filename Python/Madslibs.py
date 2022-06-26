# Concatenar cadenas de caracteres
# Supongamos que queremos crear una cadena que dija
# Aprende a programar con:___________.

# organizacion = "freecodecamp"

# print ("Aprende a programar con: " + organizacion)
# print ("Aprende a programar con {}".format(organizacion))
# print (f"Aprende a programar con {organizacion}") #f-string

print("¡Bienvendio(a)!")
adjs = input("Escribe un adjetivo: ")

verbo1 = input("Escribe un verbo: ")

verbo2 = input("Escribe un verbo: ")

sustantivo_plural = input("Escribe un sustantivo en plural: ")


Madslibs = f"¡Programar es tan {adjs}! Siempre me emociona porque me encanta {verbo1} problemas. ¡Aprender a {verbo2} con freecodecamp y alcanzar tus {sustantivo_plural}!"

print(Madslibs)
