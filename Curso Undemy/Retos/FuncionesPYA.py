print ("Funciones con parametros y argumentos")

def informacion(nombre= "Desconocido",edad= "Desconocido"): # 1. Se pasan los parametros
    print (f"Hola {nombre}")      # 2. Se pasan los parametros en el cuerpo de la funcion
    print (f"Tengo {edad} años")

informacion("Luis ", 18)     # 3. Se pasan los 'ARGUMENTOS' cuando se llama ala funcion
informacion("Luna ", 9)
informacion() # cuando se necesitan 2 argumentos y el usuario es escribe uno solo se le da un valor por 'default'