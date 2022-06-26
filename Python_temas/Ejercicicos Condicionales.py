# Ejercici 1
# Hacer un programa que pida 2 numeros y se de cuenta cual de ellos es par o si ambos son par.

#num1 = int(input("Digite un numero positivo: "))
#num2 = int(input("Digite un numero positivo: "))

# Solucion 1
"""
if num1%2==0:
	print ("El primer numero es par")
if num2%2==0:
	print ("El segundo numero que digito es par")
if num1 %2==0 and num2%2==0:
	print ("Ambos numeros son par")
elif num1%2!=0 and num2%2!=0:
	print ("Ambos numeros son impar")
"""

# Solucion 2
"""
if num1%2==0 and num2%2==0:
	print (f"Ambos numeros {num1} y {num2} son par")
elif num1%2==0 and num2%2!=0:
	print (f"El numero {num1} es par")
elif num1%2!=0 and num2%2==0:
	print (f"El numero {num2} es par")
else:
	print (f"Ambos numeros {num1} y {num2} son impar")
"""

# Ejercicio 2
# Realizar un programa que pida 3 numeros y determine cual es mayor
"""
num1 = input("Digite un numero: ")
num2 = input("Digite un numero: ")
num3 = input("Digite un numero: ")

if num1 >= num2 and num1 >= num3:
	print (f"Numero {num1} es mayor que el {num2} y {num3}")
elif num2 >= num1 and num2 >= num3:
	print (f"Numero {num2} es mayor que el {num1} y {num3}")
elif num3 >= num1 and num3 >= num2:
	print (f"Numero {num3} es mayor que el {num1} y {num2}")
"""

# Ejecicio 3
# Hacer un programa que pida un caracter e indique si es una vocal o no
"""
caracter = input("Digite un caracter en: ").lower()       # Esta funcion transforma el caracter en minusculas

if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
	print ("Es una vocal")
else:
	print ("No es una vocal")
"""
# Ejercicio 4
# Construir un programa que simule una calculadora con las 4 operaciones basicas (suma, resta, multiplicacion y division)
# el usuario debe especificar con el primer caracter la operacion que desea hacer con los numeros dados.
"""
num1 = int(input("Digite un numeros: "))
num2 = int(input("Digite un numeros: "))
operacion = input("Digite un el primer caracter de la operacion que desea realizar: \n S=suma, R=resta, M=multiplicacion, D=division \n: ").upper()

if operacion== "S":
	suma = num1+num2
	print(f"\nLa suma es: {suma}")

if operacion== "R":
	resta = num1-num2
	print(f"\nLa resta es: {resta}")


if operacion== "M":
	mult = num1*num2
	print(f"\nLa multiplicacion es: {mult}")

if operacion== "D":
	division = num1/num2
	print(f"\nLa division es: {division:.2f}")
else:
	print ("Se equivoco de operacion")
"""

# Ejercicio 5
# Hacer un programa que simule un cajero automatico con un saldo inicial de $1_000 y tendra el siguiente menu de opciones
"""
1. Ingresa dinero en la cuenta 
2. Retira dinero de la cuenta
3. Mostrar saldo disponible
4. Salir
"""
print ("'Bienvenido al cajero automatico'")
saldo = 1000

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

else:
	print("Error. Opcion del menu incorrecto!!")