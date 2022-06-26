base_datos = {}
codigo = 0

def ProgramaSena():
    print()
    print ("Programa de verificacion de estado del curso del aprendiz")
    print()
    codigo = int(input("Digite codigo salida: "))
    while codigo !=123: 
        print ("1. Menu del intructor")
        print ("2. Menu del aprendiz")
        print ("3. Salir")
        print()
        seleccion = int(input("Digite una seleccion del menu: "))
        print()
        
        if seleccion == 1:
            print ("Combrobacion de identidad de Intructor")
            print()
            usuario = input("Digite su usuario: ")
            contraseña = input("Digite su contraseña: ")
            if usuario == "Oscar" and contraseña == "Oscar123":              
                while usuario != "Oscar":
                    print ("Usuario incorrecto")
                    usuario = input("Digite su usuario: ") 
                while contraseña != "Oscar123":
                    print ("Contraseña incorrecta")                          
                    contraseña = input("Digite su contraseña: ")
            print ("Acceso admitido")
            print()
            print ("Menu del Intructor")
            print ("1. Agregar alumno a la base de datos")
            print()
            opcion = int(input("Digite una opcion del menù: "))
            if opcion == 1:
                nombre = input("Digite nombre del aprendiz: ")
                nota_act = float(input("Digite nota general de las actividad: "))
                while nota_act > 5:
                    print("Nota invalida")
                    nota_act = float(input("Digite nota general de las actividad: "))
                print ("Nota valida")
                nota_exp = float(input("Digite nota general de las exposiciones: "))
                while nota_exp > 5:
                    print("Nota invalida")     
                    nota_exp = float(input("Digite nota general de las exposiciones: "))
                print ("Nota valida")
                examen_final = float(input("Digite examen final: "))
                while examen_final >5:
                    print("Nota invalida")   
                    examen_final = float(input("Digite examen final: "))
                print ("Todas las son validas")
                print()
                print ("Sistema de evaluacion '> 3 = Aprobado' y '> 3 No aprobado'")
                print()
                nota_act = nota_act * 0.3
                nota_exp = nota_exp * 0.3
                examen_final = examen_final * 0.4
                promedio = nota_act + nota_exp + examen_final
                if promedio >=3 and promedio <=5 :
                    promedio = "Aprobado"
                elif promedio > 0 and promedio <3:       
                    promedio = "No aprobado"
                else:
                    print ("Ingrese notas validas")
                if nombre not in base_datos:
                    base_datos[nombre] = promedio
                    print("Aprendiz guardado")
                else:
                    print("Aprendiz existente")
                    print ()
                    
                    
   
        if seleccion == 2:
            print ("Comprobacion de identidad de Aprendiz")
            print()     
            ficha = int(input("Digite ficha del programa: "))
            if ficha == 2503106:             
                while ficha != 2503106:
                    print ("Ficha de caracterizacion incorrecta")
                    ficha = int(input("Digite ficha del programa: "))
            print ("Ficha correcta, Bienvendio a la plataforma de 'ADSO-4'  ")
            print()   
            print ("Menu del Aorendiz")
            print ("1. Ver estado del curso")
            print()
            opcion = int(input("Digite una opcion del menù: "))
            if opcion == 1:
                for clave,valor in base_datos.items():
                    print (f"Nombre: {clave}, Estado: {valor}")
                    
                    

        if seleccion == 3:
            print("cesion cerrada")   
            break        
    else:
        print("Gracias por utlizar el servicio!!")       
        
ProgramaSena ()