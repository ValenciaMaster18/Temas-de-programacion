"""
Ejercicio 1
Escribir un programa
que pregunte el nombre del usuario en la consola
y un número entero e imprima por pantalla
en líneas distintas el nombre del usuario tantas veces como el número introducido.


nombreDelUsuario = input ("¿Cómo te llamas?  ")
numEntero = int(input("Digite un numero entero: "))

print ((nombreDelUsuario + "\n") * int(numEntero))
"""
"""
Ejercicio 2
Escribir un programa que pregunte el nombre completo del usuario en la consola
y después muestre por pantalla el nombre completo del usuario tres veces,
una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y d
e los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""
"""
nombre = input("Intoducir nombre completo: ")

print(nombre.lower())
print(nombre.upper())
print(nombre.title())
"""
"""
Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola
y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> 
letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre


nombre = input("¿Como te llamas? ")
print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")
"""
"""
Ejercicio 4
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension
donde el prefijo es el código del país +34, y
la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
Escribir un programa que pregunte por un número
de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión
"""
"""
telefono = input("Digite su numero con el siguiente formato +xx-xxxxxxxxx-xx: ")
print ("Su numero de telefono es: " , telefono[4:-3])
"""
"""
Ejercicio 5
Escribir un programa que pida al usuario que introduzca una frase en la consola
 y muestre por pantalla la frase invertida.
"""
"""
frase = input("Ingrese una frase: ")
print(frase[::-1])
"""
"""
Ejercicio 6
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""
"""
frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minúscula:  ")
print(frase.replace(vocal, vocal.upper()))
"""
"""
Ejercicio 7
Escribir un programa que pregunte el correo electrónico del usuario en la consola 
y muestre por pantalla otro correo electrónico con el mismo nombre 
(la parte delante de la arroba @) pero con dominio ceu.es.
"""
"""
email = input("digite su correo electrónico \n")
print(email[:email.find('@')] + '@ceu.es')
"""
"""
Ejercicio 8
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales 
y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""
"""
precio = input("Introduce el precio del producto con dos decimales:  ")
print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')
"""
"""
Ejercicio 9
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa 
y muestra por pantalla, el día, el mes y el año.
Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

solucion 1

fecha = input("Introduzca su fecha de nacimiento con el siguiente formato  dd/mm/aaaa: \n")
print('Día', fecha[:2])
print('Mes', fecha[3:5])
print('Año', fecha[6:])

solucion 2 para la condicion 2

fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)
"""
"""
Ejercicio 10
Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
"""
"""
solucion 1
compra = input("¿Cuales productos comprastes separarlos por coma? \n")
print(compra.replace(',', '\n'))

solucion 2
cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
print('\n'.join(cesta.split(',')))
"""
"""
Ejercicio 11
Escribir un programa que pregunte el nombre el un producto
su precio y un número de unidades
y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros 
y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""
"""
producto = input('Introduce el nombre del producto: ')
precio = float(input('Introducde el precio unitario: '))
unidades = int(input('Introduce el número de unidades: '))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))
"""