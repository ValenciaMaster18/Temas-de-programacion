# Diicionario vacio
from tkinter import E


equipos = {}
# Agregar elementos a un diccionario vacio
equipos ["Quindio"] = 1
equipos ["Cucuta"] = 1
equipos ["Pasto"] = 1
equipos ["Union magdalena"] = 1
equipos ["Tolima"] = 5
equipos ["Once caldas"] = 5
equipos ["Independiente medelli"] = 8
equipos ["Deportivo cali"] = 12
equipos ["Junior"] = 13
equipos ["Independiente santa fe"] = 17
equipos ["America de cali"] = 17
equipos ["Millonarios"] = 19
equipos ["Nacional"] = 30

# Ver el valor
print(equipos["America de cali"])
# Modificar un valor
equipo = equipos["Junior"] = 25
# Eliminar una clave con su valor
del equipos["Nacional"]
# Agregar nuevos pares clave valor
equipos["Barcelona"] = 91
# Mezclar diccionario con strings
print(f"Soy hincha del {equipos['Junior']}")
# Ver el diccionario
print(equipos)
# Acceder a un valor
print(equipos.get(8,"No exite"))
# Iterar un diccionario clave valor
for clave,valor in equipos.items():
    print(clave,"Cantidad de titulos ",valor)
# Iterar un diccionario clave  
for clave in equipos.keys():
    print (clave)
 # Iterar un diccionario valor  
for valor in equipos.values():
    print(valor)