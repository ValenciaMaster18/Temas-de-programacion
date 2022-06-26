print("Programa de becas año 2022")

Distancia_escuela =int(input("Introduce la distancia a la escuela en km: "))
print ("Distancia_escuela")

Numero_de_hermanos=int(input("Introduce el numero de hermanos en el centro: "))
print ("Numero_de_hermanos")

Salario_familiar=int(input("Introduce salario anual bruto: "))
print ("Salario_familiar")

if Distancia_escuela > 40 and Numero_de_hermanos > 2 or Salario_familiar <= 20000:
	print("Tienes derecho a beca")
else:
	print("No Tienes derecho a beca")