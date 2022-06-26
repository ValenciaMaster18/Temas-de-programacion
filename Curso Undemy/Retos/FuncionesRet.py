mensaje = "Bienvenido"
def Mensaje(mensaje , nombre):
    return mensaje + nombre 

mensaje = Mensaje(mensaje, " Luis ")
print(f"{mensaje}")

def ultimaAct(actividad):
    return actividad
accion = ultimaAct("Comer")
print(f"Mi ultima actividad fue {accion}")