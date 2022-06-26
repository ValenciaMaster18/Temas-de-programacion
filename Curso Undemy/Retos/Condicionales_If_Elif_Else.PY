print ("Condicionales anidados")
print ("Rango de edad")
edad = int(input("Digite su edad: "))

while edad <0:
    edad = int(input("Digite su edad: "))   
if edad > 0 and edad <= 10:
    print ("Es una edad de niño")
elif edad >= 11 and edad <=18:
    print ("Es un adolecente")
elif edad > 18 and edad <= 50:
    print ("Es un adulto")
elif edad > 50 and edad <= 125:
    print ("Es un adulto mayor")
else:
    print ("Rango de edad no registrado en la base datos. Vuelva a intentarlo")