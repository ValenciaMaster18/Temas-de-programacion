print("Condicionales if y else")

dinero = 500

if dinero > 300 :
    print ("Dinero suficiente")
else:
    print ("Saldo insufiente")

# Evaluar un texto co if    
clave = "Luis"

if clave == "Luis":
    print ("Clave correcta")
else:
    print ("Clave incorrecta")

# Evaluar un boolean    
hombre = True

if hombre:
    print ("Genero valido")
else:
    print ("Genero invalido")
    
edad = 1

if edad != 0 and edad >0:
    print ("Edad valida")
else:
    print ("Edad invalida")
    
# Evaluar una lista
lenguajes = ["Python","Java","Javascript","C","C++"]

if "Python" in  lenguajes:
    print ("Python si esta en la lista")
else:
    print ("Python no esta en la lista")