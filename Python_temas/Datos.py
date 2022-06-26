
"""
1. Diseñe un algoritmo que lea los siguientes datos de una persona: nombre, sueldo mensual, edad y 
sexo. 

A continuación, el algoritmo deberá clasificar a la persona en alguna de las siguientes 
categorías: 

a) Hombre con bajos ingresos. Aquellos hombres cuyo sueldo sea inferior a 
$1.200.000/mes.

b) Mujer con altos ingresos. Las mujeres cuyo sueldo supere los $4.000.000/mes. 

c) Joven mujer de clase media. Mujer cuya edad esté comprendida entre los 20 y los 30 años y cuyo 
sueldo esté entre $1.200.000 y $4.000.000/mes.
"""
print("Clasisficacion de ingresos")

print("El programa es para saber su clasificacion de ingresos.")

Nombre_del_usuario = input("Introducir su nombre completo: ")

Sueldo_mensual = int(input("Introducir su salario mensual: "))

Edad_del_usuario = int(input("Introducir su edad:  "))

Sexo_del_usuario = int(input("""seleccione su sexo: \nMasculino (1) femenino (0): """))

if Sexo_del_usuario == 1 and Sueldo_mensual < 1_200_000: 
	print("Hombre con bajos Ingresos bajos")

if  Sexo_del_usuario == 0 and Sueldo_mensual > 4_000_000: 	
	print ("Mujer con altos Ingresos")

if Sexo_del_usuario == 0 and Edad_del_usuario >= 20 and Edad_del_usuario <= 30 and Sueldo_mensual >= 1_200_000 and Sueldo_mensual <= 4_000_000:
	print("Joven mujer de clase media")

else:
	print ("¡Su rango salarial no esta entre los encuestados!")

print ("Proceso finalizado")



