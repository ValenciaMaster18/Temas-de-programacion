print("Contar")

contar = int(input("Digite hasta que numero desea contar: "))
saltos = int(input ("Digite de cuanto en cuanto va contar: "))

count = 0

if contar >= 0:
    while count <= contar:
        print ("N° {}".format(count))
        count += saltos
else:
    print ("N° {} invalido".format(contar))