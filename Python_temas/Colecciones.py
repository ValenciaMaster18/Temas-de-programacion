# Ejercicio 1
# Escriba un programa donde tenga una lista y que, a continuacion, elimine los elementos repetidos, po ultimo mostrar la lista

name = ["Natalia", "Maria", "Yohanis", "Camila", "Lorna", "Tatiana", "Karol", "Natalia"]

conjunto = set(name)     # Convertimos la lista a conjuntos. Porque los conjuntos no pueden tener elementos iguales
name = list(conjunto)    # Despues convertimos el conjunto a lista nuevamente

name = list(set(name))   # De esta forma podemos hacerlo con una sola linea de codigo

print (name)

# Ejercicio 2
# Escriba un programa que tenga 2 listas.Con las siguientes condiciones(No debe haber repeticiones)
#Listas de elementos que aparecen en las dos listas
#Listas de elementos que aparecen en la primera, pero no en la segunda
#Listas de elementos que aparecen en la sengunda, pero no en la primera
#Listas de elementos que aparecen en ambas listas

lista1 = [1,2,3,4,5,6,7,0]
lista2 = [2,5,6,8,9,9]

# Eliminar los elementos repetidos entre ambas listas
a = set(lista1)
b = set(lista2)

union = list(a | b)
soloA = list(a - b)
soloB = list(b - a)
Interseccion = list(a & b)

print (f"Listas de elementos que aparecen en las dos listas son: \n{union}")
print (f"Listas de elementos que aparecen en la primera, pero no en la segunda son: \n{soloA}")
print (f"Listas de elementos que aparecen en la sengunda, pero no en la primera son: \n{soloB}")
print (f"Listas de elementos que aparecen en ambas listas son: \n{Interseccion}")

# Ejercicio 3 - creando personajes dentro de una lista

personajes = []

p = {"Nombre":"Luis Diaz","Numero":23,"Profesion":"Futbolista"}
personajes.append(p) # Agregamos a la lista el personaje

p = {"Nombre":"La valdiri", "Numero":1,"Profesion":"Influencer"}
personajes.append(p) # Agregamos a la lista el personaje

p = {"Nombre":"Sebastucho", "Numero":10,"Profesion":"Influencer"}
personajes.append(p) # Agregamos a la lista el personaje

print()
print(personajes)
print()
print(type(personajes))