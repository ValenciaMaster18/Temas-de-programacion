print ("Asignaturas año 2022")
print ("Asignaturas optativas: programacion de sofware - tecnico en sistemas - programador web")

Opcion= input("Escribe la Asignatura escogida: ")

Asignatura=Opcion.lower()

if Asignatura in ("programacion de sofware", "tecnico en sistemas" , "programador web"):
	print ("Asignaturas elegida: " + Asignatura)
else:
    print("la Asignatura elegida no esta complementada")