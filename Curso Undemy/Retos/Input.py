print ("Examen de cultura general")
 
examen = 0
pregunta = int(input(f"Hola para salir del programa escriba -<<<< Si (0) No (1): "))

while pregunta != 0: 
        
    name = input("¿Cual es tu nombre?\n").capitalize()
    answer1 = input("¿Cual es la capital de colombia?\n").capitalize()
    answer2 = int(input("¿Cuanta esrellas tiene la bandera de estados unidos?\n"))
    answer3 = float(input("¿Cuando fue la primera guerra mundial?\n"))
    answer4 = input("¿Cual es el pais mas grande del mundo?\n").capitalize()
    answer5 = input("¿Cual es el  pais mas pequño del mundo?\n").capitalize()
    if answer1 == "Bogota":
        print ("Pregunta 1 correcta!!")
        examen += 2
    else:
        print ("Respuesta 1 incorrecta. La respuesta era 'Bogota'")
    if answer2 == 50:
        print ("Pregunta 2 correcta!!")
        examen += 2
    else:
        print ("Respuesta 2 incorrecta. La respuesta era '50'")
    if answer3 == 1914:
        print ("Pregunta 3 correcta!!")
        examen += 2
    else:
        print ("Respuesta 3 incorrecta. La respuesta era '1914'")
    if answer4 == "Rusia":
        print ("Pregunta 4 correcta!!")
        examen += 2
    else:
        print ("Respuesta 4 incorrecta. La respuesta era 'Rusia'")
    if answer5 == "Ciudad del vaticano":
        print ("Pregunta 5 correcta!!")
        examen += 2
    else:
        print ("Respuesta 5 incorrecta. La respuesta era 'Ciudad del vaticano'")
    if examen >= 6 and examen <=10:
        print (f"Examen aprobado tu calificacion fue de {examen}")
        pregunta = int(input(f"Hola para salir del programa escriba -<<<< Si (0) No (1): "))
    else:
        print (f"Examen No aprobado tu calificacion fue de {examen}")
        pregunta = int(input(f"Hola para salir del programa escriba -<<<< Si (0) No (1): "))

else:
    print("Salistes del programa!!")