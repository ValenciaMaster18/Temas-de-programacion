Salario_presidencial=int(input("Introduce salario presidente: "))
print ("Salario presidente: " + str(Salario_presidencial))

Salario_director=int(input("Introduce salario director: "))
print ("Salario presidente: " + str(Salario_director))

Salario_jefe_area=int(input("Introduce salario jefe de area: "))
print ("Salario presidente: " + str(Salario_jefe_area))

Salario_administrativo=int(input("Introduce salario administrativo: "))
print ("Salario presidente: " + str(Salario_administrativo))

if Salario_administrativo<Salario_jefe_area<Salario_director<Salario_presidencial:
	print("Todo funciona correctamente")
else:
	print ("Algo funciona mal en esta empresa")