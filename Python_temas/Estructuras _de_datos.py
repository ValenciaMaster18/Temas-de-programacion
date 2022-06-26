"""
Estructuras de datos:

Las mas comunes son: las listas, las tuplas y los diccionarios.

LAS LISTAS: Las listas en Python son en esencia una colección de elementos, no necesariamente del mismo tipo.
Su característica principal reside en que el orden de sus elementos se mantiene en todo momento. 
Las listas usan corchetes ([]) para encerrar a sus elementos, y comas (,) para separarlos.

LAS TUPLAS: Una tupla es una colección de objetos ordenados que encierra sus elementos con paréntesis () 
y los separa con comas. Las tuplas son muy similares a las listas, y pueden almacenar objetos de tipo distinto
como enteros y strings entre otros. Sin embargo, al contrario que las listas presentan 
la propiedad de inmutabilidad Esto implica que los elementos de una tupla no pueden reasignarse.

LOS DICCIONARIOS: Los diccionarios almacenan pares de objetos clave-valor. En contraste con las listas, 
los diccionarios no garantizan que se mantenga el orden en que sus objetos han sido almacenados. Además, 
en un diccionario el acceso a un objeto se realiza indicando la clave de ese objeto. Este es otro elemento 
diferenciador entre diccionarios y listas, donde el acceso a los objetos se realiza indicando
la posición que ocupan. Los diccionarios utilizan llaves ({}) para encerrar a sus elementos, y dos puntos (:)
 para indicar las claves y sus valores asociados.
 """

# Mi LISTA:

#
#print ("Bienvenidos al SENA")
#print ("Este es el listado de los alumnos aprobados en el Tecnologo de ADSO")

# Indice        0        1         2        3           4         5        6        7         8... 

#Aprobados = ["Luis", "Eduardo", "Caleb", "Daniel", "Cristian", "Angel","Vanessa","Daniel", "Pedro"]
#
#Aprobados.append("Willian smith") # Agrega un ítem al final de la lista

#print (Aprobados.index("Luis")) # Retorna el índice basado en cero del primer elemento cuyo valor sea igual a x.

#Aprobados.extend(["Alfonso", "Regina"]) # Extiende la lista agregándole todos los ítems del iterable.

#print(Aprobados.count("Daniel")) # Retorna el número de veces que x aparece en la lista.

#Aprobados.remove("Eduardo") # Quita el primer ítem de la lista cuyo valor sea x.

#Aprobados.pop() # elimina y retorna un elemento de una lista. Puede emplear un parámetro opcional, que el índice del elemento que desea eliminar de la lista.

#Aprobados.insert(0, "Diaz") # Inserta un ítem en una posición dada. El primer argumento es el índice del ítem delante del cual se insertará.

#Aprobados.clear() # Elimina todos los elementos de la lista.

#Aprobados.sort() # Ordena los elementos de la lista

#print(Aprobados.copy()) # Retorna una copia superficial de la lista.

#Aprobados [4] = "Cesar"  # Este metodo nos permite modificar un elemento de la lista.

#print ("Daniel" in Aprobados) # este metodo nos permite saber si ese elemento se encuentra en la lista.

#print (len(Aprobados)) # Esta funcion nos sirve saber el numero de elementos.

#print (Aprobados)


#def obtener_número_de_elementos(list):                                                # Esta es una forma en la que podemos saber 
#    count = 0
#    for element in list:                                                              # el numero de elementos que hay en la lista               
#        count +=  1                                                                   #  un "usando el bucle for"  
#    return count
#
#print("Número de elementos de la lista: ", obtener_número_de_elementos(Aprobados))
#
#
#print ("Felicidades por aprobar, estas en una gran institucion!!")
#
#print (type(Aprobados)) # Se utila para saber el tipo de dato

# Ejemplo de Listas con algunos metodos.

#fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']


#print(fruits.count('apple'))

#print(fruits.count('tangerine'))

#print(fruits.index('banana'))

#print(fruits.reverse())

#print(fruits.append('grape'))

#print(fruits.sort())

#print(fruits.pop())

#print (fruits)

# MI TUPLA:

#print ("Mis valores")

#Valores = ("Respeto","Honestidad","Responsabilidad","Humildad") # Las tuplas pueden ir sin parentesis

#print (Valores [0])                                            # Formula para acceder a un elemento de una tupla.

#print (Valores [:])                                            # Formula para acceder a un subconjunto de elementos.



#for Valor in Valores:              # El bucle for en Python es una de las estructuras ideales para iterar sobre  
#    print (Valor)                  # los elementos de una secuencia. ideales para iterar sobre los elementos de una secuencia. 



#print(len(Valores))                # a función len(). Esta función devuelve el número de elementos de una tupla.


#if "Honestidad" in Valores:         #  para saber si un elemento está contenido en una tupla, se utiliza el operador de pertenencia "in".
#    print ("Si")
#
#
#if "Lealtad"  not in Valores:
#    print("No")     





#print(Valores.count("Respeto")) #  cuenta el número de veces que el elemento x está en la tupla.

#print(Valores.index("Respeto")) #  la forma más fácil de encontrar la posición de un elemento dentro de una lista de Python. 
                                 #  Aunque, esta función solo devuelve el índice de la primera aparición del valor dado.
#print (Valores)

#print (type(Valores))


# Ejemplo de como modificar una tupla:
#as tuplas son objetos inmutables. No obstante, las tuplas pueden contener objetos u otros elementos de tipo secuencia, por ejemplo, una lista. 
#Estos objetos, si son mutables, sí se pueden modificar:



#tupla = (1, ['a', 'b'], 'hola', 8.2)
#
#tupla[1].append('c')                             # tupla[1] hace referencia a la lista
#
#print (tupla)


# Mi DICCIONARIOS:

"""
LOS OBJETOS INMUTALES:
    
    Las tuplas
    Los enteros
    Los flotantes              Todos estos son objetos inmutables y se pueden usar para armar un diccionario
    Los booleanos
    Los stings
"""

print ("Datos privados")


Mis_datos = {"Nombre": "Luis", 
            "Numero de documento": 1001892059, 
            "Edad": 18, 
            "Estatura": 1.80, 
            (2003, 2012, 2021): "Mis fechas importantes"
}



#print(Mis_datos.keys())                    # Metodo para ver mis claves del "dic". Tambien podemos usar 
#print(list(Mis_datos.keys()))              # la funcion list o tuple para ver las claves en esa forma
#print(tuple(Mis_datos.keys()))   


#print(tuple(Mis_datos.values()))           # Si queremos ver los valores de las claves usamos este metodo "values"


#print(tuple(Mis_datos.items()))            # Si queremos ver el par vlave:valor usamos el metodo "items" 



#print (Mis_datos)

#print (type(Mis_datos))































