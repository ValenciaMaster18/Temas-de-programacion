
class Sena:
    base_datos = {}
    def __init__(self, nombre = "Default", nota_act = 0.0, nota_exp = 0.0, examen_final= 0.0):
        Sena.base_datos [nombre] = examen_final
        self.nombre = nombre
        self.nota_act = 0.0
        self.nota_exp = 0.0
        self.examen_final = 0.0
              

    def validacion(self):
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
        if self.nombre not in Sena.base_datos:
            Sena.base_datos[self.nombre] = promedio
            print("Aprendiz guardado")
        else:
            print("Aprendiz existente")
            print ()


    
    def validacionIntructor(self):
        print ("Combrobacion de identidad de Intructor")
        print()
        usuario = input("Digite su usuario: ")
        contraseña = input("Digite su contraseña: ")              
        while usuario != "Oscar":
            print ("Usuario incorrecto")
            usuario = input("Digite su usuario: ") 
        while contraseña != "Oscar123":
            print ("Contraseña incorrecta")                          
            contraseña = input("Digite su contraseña: ")
            if usuario == "Oscar" and contraseña == "Oscar123":
                print()   
        print ("Acceso admitido")
                

    def menuIntuctor (self):
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
            
            
    def validacionAprendiz(self):
        print ("Comprobacion de identidad de Aprendiz")
        print()     
        ficha = int(input("Digite ficha del programa: "))
        if ficha == 2503106:             
            while ficha != 2503106:
                print ("Ficha de caracterizacion incorrecta")
                ficha = int(input("Digite ficha del programa: "))
        print ("Ficha correcta, Bienvendio a la plataforma de 'ADSO-4'  ")
        print()   
  
    
    def menuAprendiz (self):
        print ("Menu del Aorendiz")
        print ("1. Ver estado del curso")
        print()
        opcion = int(input("Digite una opcion del menù: "))
        if opcion == 1:
            for clave,valor in Sena.base_datos.items():
                print (f"Nombre: {clave}, Estado: {valor}")
                
    
def menuGeneral():
        codigo = 0
        print ()
        print ("Programa de verificacion de estado del curso del aprendiz")
        print()
        print ("1. Menu del intructor")
        print ("2. Menu del aprendiz")
        print ("3. Salir")
        print()
        seleccion = int(input("Digite una seleccion del menu: "))
        print()
        codigo = int(input("Digite codigo salida: "))
        while codigo !=123: 
            if seleccion >= 1 and seleccion <=3:             
                if seleccion == 1:
                    objeto = Sena ()
                    print(objeto.validacionIntructor())
                    print(objeto.menuIntuctor())
                    print(objeto.validacion())  
                    print(objeto.validacionAprendiz())
                    print(objeto.menuAprendiz())
                        

                if seleccion == 3:
                    print("Gracias por utlizar el menu general!!")

            else:
                print("Opcion del menu incorrecta")
                break
        else:
            print("Gracias por utlizar el servicio!!")  

menuGeneral()
            

    
    


