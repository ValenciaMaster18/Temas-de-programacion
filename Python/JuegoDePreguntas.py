print ("Bienvenido al quiz")

nom = input ("Introducir tu nombre: ")
Unirse = input("Quieres jugar al juego: " ).lower()

if Unirse != "si":
    quit()
    
print (f"Hello {nom} Bienbenido al juego !!")

calificacion = 0

pregunta = int(input ("¿Cuantas estrellas tiene junior? "))

if pregunta == 9:
    print ("Respuesta correcta!!")
    calificacion += 1
else:
    print("Respuesta incorrecta!!")

pregunta = input("¿Cuando fue fundado el junior? ").lower()

if pregunta == "7 de agosto de 1924":
    print ("Respuesta correcta")
    calificacion += 1
else:
    print ("Respuesta incorrecta")

pregunta = input ("¿Nombre del estadio del junior? ").capitalize()

if pregunta == "Estadio metropolitano roberto melendez":
    print ("Respuesta correcta")
    calificacion += 1
else:
    print ("Respuesta incorrecta")

pregunta = input("¿Quien creo junior? ").capitalize()

if pregunta == "Micaela" or pregunta == "Micaela lavalle de mejia":
    print ("Respuesta correcta")
    calificacion += 1
else:
    print ("Respuesta incorrecta")

pregunta = input ("¿Quien es el maximo goleador del junior? ").capitalize()

if pregunta == "Ivan rene valenciano":
    print ("Respuesta correcta")
    calificacion += 1
else:
    print ("Respuesta incorrecta")

print (f"Total respuestas correctas: {calificacion}")
print (f"La nota final del quiz es: {calificacion/5*100} % ")










































































































































