def validacion(nota_act, nota_exp, examen_final):
        
    nota_act = nota_act * 0.3
    nota_exp = nota_exp * 0.3
    examen_final = examen_final * 0.4
    promedio = nota_act + nota_exp + examen_final
        
    if promedio >=3:
        print ("Aprobado")

    else:
        print ("No aprobado")
            
    
    
    
print ("1. Agregar alumno a la base de datos")
print ("2. Eliminar alumno a la base de datos")
print ("3. Salir")
opcion = int(input("Digite una opcion del menù: "))
if opcion == 1:
    nombre = input("Digite nombre del aprendiz: ")        
    nota_act = float(input("Digite nota general de las actividad: "))
    nota_exp = float(input("Digite nota general de las exposiciones: "))
    examen_final = float(input("Digite examen final: "))
    validacion(nota_act, nota_exp, examen_final)

    