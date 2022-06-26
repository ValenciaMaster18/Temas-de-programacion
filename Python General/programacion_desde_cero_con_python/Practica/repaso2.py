
#ELEMENTOS BASICOS EJERCICIOS 

# Ejercicio 1
#Escribir la siguiente expresion en forma de expresion algoritmica

#a**3 * (b**2 - 2ac) /2ab
"""
a= int(input("Digite un numero para a: "))
b= int(input("Digite un numero para b: "))
c= int(input("Digite un numero para c: "))

resultado = (a**3 * (b**2 - 2*a*c))/(2*b)
print(f"El resultado es:  {resultado}")
"""
# Ejercicio 2
# Determinar la solucion logica de la siguiente operacion
#((3 + 5 * 8) < 3 and ((-6/3 * 4) + 2 < 2)) or (a > b)
"""
a= int(input("Digite un numero para a: "))
b= int(input("Digite un numero para b: "))



if ((3 + 5 * 8) < 3 and ((-6/3 * 4) + 2 < 2)) or (a > b):
	print ("Operacion logica True")
else:
	print ("Operacion logica False")
"""
# Ejercicio 3
# Realizar un programa para intercambiar el valor de 2 variables
"""
a= int(input("Digite un numero para a: "))
b= int(input("Digite un numero para b: "))

tmp = a
a = b
b = tmp

resultado = a,b
print (f"El resultado es: {resultado}")
"""

# Ejercicio 4 
# Hacer un programa para ingresar el radio de un circulo y se reporte su area y la longitud de la circunferencia
"""
print ("Programa para calcular el area y longitud de un circulo")

import math

radio = float(input("Ingrese el radio de el circulo en cm: "))

area = math.pi * radio**2
longitud = 2 * math.pi * radio

print (f"El area del circulo es: {area:.2f}")                  # Con :.2f le estoy indicando cuantos decimales quiero despues del punto
print (f"La longitud de la circunferencia es: {longitud:.2f}")
"""

# Ejercicio 5
# Una tienda ofrece un descuento del 15% sobre el total  de la compra 
# un cliente desea saber cuanto debera pagar finalmente por su compra

precio= int(input("¿Cuanto fue el total de la compra? \n: "))

descuento = precio * 0.15
precioFinal = precio - descuento

print (f"El precio que usted debe pagar es un total de $ {precioFinal:.0f}")



