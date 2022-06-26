# Ejercicio 1
# llenar la lista con los numeros desde el numero 1 hasta el 50
# luego mostrar la lista con los bucles for, los elementos deben mostrarse de la siguiente forma
# 1-2-3-4-5...50
"""
lista = []

i = 1 
# Agregamo elementos a la listas desde el 1 al 50.

while i <=50:
	lista.append(i)
	i += 1

# Imprimiendo los elementos de la lista

for i in lista:
	print(i,end= "-")
print(type(i))
"""
# Solucion 2
"""
lista = list(range(1,51))


for i in lista:
	print(i,end= "-")
print(type(i))
"""
# Ejercicio 2 
# llenar una lista con los numeros desde el 1 al 10
# luego modificar los elementos de lista multiplicandolos por un valor que digite el usuario
"""
lista = list(range(1,11))

print("La lista original es: ")

for i in lista:
	print(i,end= "-")

valor = int(input("\nDigite un valor a multiplicar la lista: \n"))
# Multiplicar los elementos de la lista.

for indice,i in enumerate(lista):
	lista[indice] *= valor

for i in lista:
	print(i,end="-")
"""
# Ejercicio 3
# Pide un numero y metelos en una lista, cuando el usuario meta un cero 0 ya dejamos de insertar.
# por ultimo, muestra los numeros ordenados de menor a mayor
"""
lista = []

salir = False

while not salir:
	valor = int(input("Digite un numero: "))

	if valor == 0:
		salir = True
	else:
		lista.append(valor)

lista.sort()

print(f"La lista ordenada es: \n{lista}")
"""
# Ejercicio 4
# Hacer un programa para sumar numeros pares dentro de un rango.
# Ejemplo 
#	suma de numeros pares del 2 al 30	
#	suma = 240
"""
a = int(input("Digite de donde va a comenzar a sumar: "))
b = int(input("Digite hasta donde quiere llegar de sumar: "))
suma = 0

for i in range(a,b+1):
	if i%2==0:
		suma += i


print(f"La suma de numeros pares del rango es: {suma}")
"""
# Ejercicio 5
# Hacer un programa para calcular el factorial de un numero positivo
"""
a = int(input("Digite el numero que desea conocer el factorial: "))

while a<0: # Mientras el numero sea negativo se ejecuta esta condicion
	print("Error. El numero tiene que ser positivo")
	a = int(input("Digite el numero que desea conocer el factorial: "))

# Calcular el factorial empieza desde uno porque todo numero multipilcado por 0 da cero.
factorial = 1 
for x in range(1,a+1):
	factorial *= x

print(f"El factorial del numero es: {a} es {factorial}")
"""
# Ejercicio 6
# Hacer un programa que pida un numero por teclado y guarde en una lista su tabla de multiplicar del 1 al 10
"""
num = int(input("Digite el numero que desea multipilicar: \n"))

lista = []

for x in range(1,10+1):
	lista.append(x*num)

print (f"\n Tabla de multiplicar es: \n{lista}")
"""
# Ejercicio 7
# Realizar un juego para adivinar un numero. Para ello generar un numero aleatorioentre 0-100, 
# y luego ir pidiendo numeros indicados "Es mayor" o  "Es menor" segun sea mayor o menor con respecto a N
# El proceso termina cuando el usuario adivina el numero y mostrar cuantos intentos hizo
"""
import random

aleatorio = random.randint(0,1000000) # Aqui generamos un numero aleatorio

print("\tJuego adivina el numero !!")

contador = 0

while True:
	numero = int(input("Digite un numero: "))
	contador += 1

	if numero >aleatorio:
		print ("\tNo es el numero: Digite un numero menor")
	elif numero < aleatorio:
		print ("\tNo es el numero: Digite un numero mayor")
	else:
		print (f"\tFelicidades, has logrado adivinar el numero {aleatorio}")
		break

print (f"Juego finalizado tu numero de intentos fue de: {contador}")
"""
# Ejercicio 8
# Hacer un programa que simule un cajero automatico con un saldo inicial de $1_000 y tendra el siguiente menu de opciones
"""
1. Ingresa dinero en la cuenta 
2. Retira dinero de la cuenta
3. Mostrar saldo disponible
4. Salir
"""
"""
print ("'Bienvenido al cajero automatico'")
saldo = 1000000
while True:

	print ("\tMenu!!")
	print("1. Ingresa dinero en la cuenta")
	print("2. Retira dinero de la cuenta")
	print("3. Mostrar saldo disponible")
	print("4. Salir")
	print ()
	
	opcion = int(input("Seleciione la opcion del menu que desea realizar: "))
	
	print ()
	
	if opcion==1:
		extra = float(input("¿Cuanto dinero desea ingresar a la cuenta? \n: "))
		saldo += extra
		print (f"Su nuevo saldo de la cuenta es de: $ {saldo:.0f}")
	
	elif opcion==2:
		retirar = float(input("¿Cuanto dinero desea retirar de la cuenta? \n: "))
		if retirar>saldo:
			print ("Saldo insuficiente")
		else:
			saldo -= retirar
			print (f"Su nuevo saldo de la cuenta es de: $ {saldo:.0f}")
	
	elif opcion==3:
		print (f"Su saldo actual de la cuenta es de: $ {saldo:.0f}")
	
	elif opcion==4:
		print ("Su seccion a cerrado")
		break
	
	else:
		print("Error. Opcion del menu incorrecto!!")

	print ()
"""
# Ejercicio 9
# Hacer un programa donde el usuario ingrese una frase, se le devolvera la misma frase pero sin espacios
# en blanco y ademas un contador de cuantos caracteres tiene la frase (sin los espacios en blanco)
"""
frase = input("Escriba una frase: ")
frase2 = ""


for x in frase:
	if x != " ":
		frase2 +=x
		
frase = frase2

print (f"Frase final: {frase}")
print (f"N° de Caracteres: {len(frase)}")
"""
# Ejercicio 10
"""
Hacer un programa que pida una cadena por teclado, luego meta los caracteres en una lista sin repetir caracteres
"""
"""
palabra = input ("Escriba una palabra: ")

lista = []

for x in palabra:
	if  x not in lista: # Si el caracter aun no esta en la lista lo agregamos a la lista
		lista.append(x) # Lo añadimos a lista 

print (f"Lista de caracteres sin repetir: \n{lista}")
"""

# Ejercicio 11
"""
Hacer un programa que simule una agenda de contacto. Crear un diccionario donde la clave
sea el nombre del usuario y el valor sea el telefono, el programa tendra el siguiente menu 
1. Nuevo contacto
2. Borrar contacto 
3. Ver contacto 
4. salir
"""

agenda = {}
                                           	                                
while True: 
	print ("\tMenu!!")
	print("1. Nuevo contacto")
	print("2. Borrar contacto ")
	print("3. Ver contacto ")
	print("4. Salir")
	opcion = int(input("Digite una opcion de menu: \n"))

	print ()

	if opcion ==1:
		nombre = input("Nombre del contacto: \n").lower()
		telefono = int(input("Numero del telefono: \n"))

		if nombre not in agenda:
			agenda[nombre] = telefono
			print ("Contacto guardado")
		else:
			prin ("Nombre existente")

	elif opcion ==2:
		nombre = input("Nombre del contacto: \n").lower()
		if nombre in agenda:
			del(agenda[nombre])
			print ("Contacto eliminado")
		else:
			print ("Contacto no existe")

	elif opcion ==3:
		print (f"Agenda de contactos: ")
		for clave,valor in agenda.items():
			print (f"Nombre: {clave}, Telefono: {valor}")

	elif opcion ==4:
		print ("Gracias por utlizar la agenda de contacto")
		break

	else:
		print ("Esa opcion del menu no existe !!")

print ()



