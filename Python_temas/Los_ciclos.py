"""
CICLO WHILE:

El ciclo while se ejecuta mientras una condición sea cierta (True)

"""




contador = 0

while contador < 50:

	print (contador)

	contador += 1 # Esta sentencia podemos abreviarla y es exactamente lo mismo que: contador = contador + 1

else:
	print ("contador si es menor que 50")	# Es opcional poner un else no es necesario.

"""
Existen dos formas de interrumpir un ciclo, la primera es con el comando continue, al ejecutarlo, el programa se 
“salta” un ciclo o iteración y continúa con la siguiente iteración. Veamos un ejemplo, en donde nos saltamos
la iteración 3
"""
# Ejemplo:

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


"""
La segunda forma de interrumpir un ciclo es con el comando break, este comando interrumpe totalmente el ciclo,
veamos el mismo ejemplo anterior, pero ahora usamos break en lugar de continue. 
"""

# Ejemplo:

for i in range(1, 6):
    if i == 3:
        break
    print(i)

"""
CICLO FOR:

un ciclo for en Python es una estructura iterativa para ejecutar un mismo segmento de código una cantidad de 
veces deseada y conocida.Pues necesitamos conoces previamente un valor de inicio, un tamaño de paso y un valor 
final para el ciclo.

La sintaxis de un ciclo for es simple en Python. En realidad, en la mayoría de los lenguajes de alto nivel es
incluso muy similar,de hecho, con tan solo tener bien claros los 3 componentes del ciclo for (inicio, final y
tamaño de paso)

for variable_contadora in range(valor_inicial, valor_final, tamaño_paso:
    ...
    ...
    Bloque de Instrucciones...
    ...
    ...

Bloque fuera del ciclo...
Como puedes ver, la magia está en la función range() de Python, pues con esta definimos desde dónde y hasta dónde 
irá el ciclo, además del tamaño del paso. De hecho, la función range(), solo necesita como mínimo el límite
superior, generando así un rango de números desde cero hasta ese límite de uno en uno. Finalmente, esta función
omite el último valor, de ese modo, el ciclo va de valor_inicial hasta valor_final - 1 
(hay que quitarle uno al valor_final).
"""
# Ejemplo 1: Mostrar en pantalla los números pares: números pares entre el número 500 y el 1000 y mostrarlos. 

# Solución inicial del ejemplo 1:

for i in range(500, 1000, 2):
    print(i)

#El código anterior funciona. Sin embargo, seguro notaste al ejecutarlo que solo mostró hasta el 998, incluso aunque 1000
#es un número par. Esto es debido a que, como indiqué, range() va hasta el límite superior - 1, así que debes sumarle 1,
#para que sea incluido, así:


for i in range(500, 1000 + 1, 2):
    print(i)

# Ejemplo 2: 
"""
Para este caso, debido a que queremos ir de un número mayor a uno más pequeño, por lo tanto, para este ejemplo el valor
inicial será 100 y el valor final será 0. Adicional, el tamaño de paso será de 1 negativo, es decir, -1, así:
"""

for i in range(100, -1, -1):
    print(i)

#Ejemplo 3:
"""
Para este caso el valor inicial será 0 y el valor final será 10000. Adicional, el tamaño de paso será de 1 
(este es el caso más común). Al interior del ciclo, en cada iteración verificaremos si elnúmero en el que
 estamos es divisible por 33 o no y en caso afirmativo aumentaremos el contador en una unidad así:
"""

contador = 0 # Iniciamos el contador en cero

for i in range(10000):
    if (i % 33 == 0): # Preguntamos si el residuo es 0 (es múltiplo de 33)
        contador += 1 # Si es múltiplo aumentamos el contador en 1
    
    # Si no es múltiplo no hacemos nada

#Mostramos el valor del contador
print(contador)

# Este ciclo for nos permitirá saber que existen 304 múltiplos del número 33 en los números del 0 al 10000 (incluido el 10000 mismo).