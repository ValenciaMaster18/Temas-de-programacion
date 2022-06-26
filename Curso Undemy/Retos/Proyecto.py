import os

CARPETA = 'Contacto/'  # Carpeta de contacto
EXTENSION = ".txt"      # Extencion de archivos
def app():
    crearDirectorio()
    mostrarMenu()

    # Preguntarle al usuario la accion a realizar
    pregunta = True
    while pregunta:
        opcion = int(input("Digite una opcion del menu: "))
        # Ejecutar las acciones
        if opcion == 1:
            agregarContacto()
            pregunta = False
        elif opcion == 2:
            print("Editar contacto")
            pregunta = False
        elif opcion == 3:
            print("Ver contacto")
            pregunta = False
        elif opcion == 4:
            print("Buscar contacto")
            pregunta = False
        elif opcion == 5:
            print("Eliminar contacto")
            pregunta = False
        else:
            print ("Opcion del menu invalida. Vuelva a intentarlo!!")  

def agregarContacto():
    print ("Escriba los datos para agregar el nuevo contacto")
    nombre_contacto = input("Nombre del contacto: ")
    # Estamos creando el archivo
    with open(CARPETA +nombre_contacto+EXTENSION,'w') as archivo: # as archivo es para referinos mas facil al archivo
        archivo.write("Nombre: " + nombre_contacto)
    
def mostrarMenu():
    print("Seleccione del menu lo que desee hacer: ")
    print("1) Agregar nuevo contacto")
    print("2) Editar contacto")
    print("3) Ver contacto")
    print("4) Buscar contacto")
    print("5) Eliminar contacto")
    
def crearDirectorio():
    if not os.path.exists(CARPETA):
        # Crear carpeta
        os.makedirs(CARPETA)
app()