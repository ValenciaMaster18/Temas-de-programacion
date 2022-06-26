print ("Evaluacion de sistema electrico")
promedio = 0
consum = 0
contador = 0
respondent_area = input("Lugar de la zona a encuestar: ")
while True:
    name_user = input("Nombre del suscriptor: ") 
    print ("Hola, " + name_user)
    try:
        contract_number = int(input("Digite numero de contrado == 5 digitos: "))
        if contract_number >= 10000 and contract_number <= 99999:
            print("Numero de contrato valido")
            subs_type = int(input("¿Cual es el tipo de suscriptor? (1) residencial (2) comercial: "))     
            if subs_type == 1 or subs_type == 2:  
                print ("Seleccion correcta")
                initial_reading = int(input("¿Cual fue la lectura inicial del medidor?: ")) 
                final_reading = int(input("¿Cuanto fue la lectua final del medidor?:  ")) 
                consumo = initial_reading - final_reading
                consum += consumo
                if subs_type == 1 and consumo >500:
                    print (f"Tu consumo es de {consumo} en Kwh. Es alto consumo energetico")
                    promedio += consumo
                    contador += 1
                elif subs_type == 2:
                    print (f"Tu consumo es de {consumo}")
                else:
                    print (f"Tu consumo es de {consumo} en Kwh")
                pregunta = input("Para salir del programa pulse 'X': " )
                if pregunta == "X":
                    break
            else: 
                print("Tiene que ser 1 o 2")
        else:
            print ("Numero de contrato invalido")
    except:
        print ("Carateres invalidos. Vuelva a intentarlo")      
promedio = promedio/contador
print (f"El promedio de la zona de suscritores residenciales de alto consumo es {promedio:.0f} Kwh")
print (f"Consumo 'Electrico Total' en {respondent_area} es de {consum} Kwh")
print (f"Encuesta finalizado en la zona {respondent_area}")