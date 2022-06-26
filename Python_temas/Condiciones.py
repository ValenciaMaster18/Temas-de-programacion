
"""
Los condiconales

Los condicionales en Python, son una estructura de control 
esencial al momento de programar y aprender a programar.
Un condicional, permite establecer una serie de condiciones
al interior de nuestro programa, que nos ayudan a determinar
qué acciones llevar a cabo dadas ciertas circunstancias.
Básicamente, tomar decisiones. 

"LAS CONDICIONES SE EVALUAN DE FORMA DESENDENTE: ARRIBA ASIA ABAJO"

Ejemplo:

si queremos decidir cuándo dar acceso a un usuario, dependiendo
de si el nombre de usuario y contraseña son correctos.
En ese caso, un condicional, nos permite verificar
si se cumple la condición de que el usuario y la contraseña 
ingresados sean lo que esperamos; y de acuerdo a que se cumpla
o no, ejecutar ciertas acciones. 
"""
"""
print ("Verificacion para entrar a la discoteca")

edad = int(input("Introducir tu edad: ")) # string   #  Tipado dinamico - int o float


if edad >= 18:                        # No puede existir un "else" si antes un "if"
	print ("Puedes pasar porque ")

elif edad < 18:
	print ("No puedes pasar poque no eres mayor de edad")  # El bloque de elif es completamente "opcional" 
"""
Bienvenidos = "Hola, bienvenidos a la clasificacion por edad!!"
print (Bienvenidos)

edad = int(input("Introducir tu edad: ")) 


if edad >= 1 and edad <= 18:                     
	print ("Eres una persona joven")
elif edad > 18 and edad <= 50:
	print ("Eres una persona adulta")
elif edad > 50 and edad <= 120:
	print ("Eres una persona mayor")
else:
	print ("No hay edad registradad en esa edad")

print ("Has finalizado el proceso")	

	