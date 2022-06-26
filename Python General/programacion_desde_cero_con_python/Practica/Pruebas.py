# for i in range(8):
#     print(i)
#     if i > 2 : 
#         print('Mayor que 2')
#         print('Terminado con i', i)
# print('Todo Terminado') 


# print ("Programa para calcular salario")
# print ()

# horasTrabajadas = int(input("¿Cuantas horas trabajo?: "))
# tarifaDeHoras = float(input("¿Cuanto vale la hora de trabajo?: "))

# if horasTrabajadas <= 40:
#     salarioNormal = horasTrabajadas * tarifaDeHoras 
#     print ("Tu salario es: " , salarioNormal)
# elif horasTrabajadas > 40:
#     tarifaDeExtras = float(input("¿Cuanto vale la hora extra?: "))
#     horasExtras = horasTrabajadas - 40
#     print (horasExtras)
#     horasSinExtras = horasTrabajadas - horasExtras 
#     print (horasSinExtras)
#     salario = horasSinExtras *  tarifaDeHoras + horasExtras * tarifaDeExtras
#     print ("Tu salario es: " , salario)

# while True:    
#     try:
#         horasTrabajadas = int(input("¿Cuantas horas trabajo?: "))
#         tarifaDeHoras = float(input("¿Cuanto vale la hora de trabajo?: "))
#         if horasTrabajadas <= 40:
#             salarioNormal = horasTrabajadas * tarifaDeHoras 
#             print ("Tu salario es: " , salarioNormal)
#             break
#         elif horasTrabajadas > 40:
#             tarifaDeExtras = float(input("¿Cuanto vale la hora extra?: "))
#             horasExtras = horasTrabajadas - 40
#             horasSinExtras = horasTrabajadas - horasExtras 
#             salario = horasSinExtras *  tarifaDeHoras + horasExtras * tarifaDeExtras
#             print ("Tu salario es: " , salario)  
#             break

#     except ValueError :
#         print ("Valor incorrecto vuelva a intentarlo!!")
        
# def calcularSalario(horasTrabajadas,tarifaDeHoras,tarifaDeExtras):  
#     while True:    
#         try:
#             horasExtras= int(horasTrabajadas)
#             tarifaDeHoras = float(tarifaDeHoras)
#             tarifaDeExtras = float(tarifaDeExtras)
            
#             if horasTrabajadas <= 240:
#                 salarioNormal = horasTrabajadas * tarifaDeHoras 
#                 print ("Tu salario es $ {:.0f} Pesos".format(salarioNormal))
#                 break
            
#             elif horasTrabajadas > 240:
#                 horasExtras = horasTrabajadas - 40
#                 horasSinExtras = horasTrabajadas - horasExtras 
#                 salario = horasSinExtras *  tarifaDeHoras + horasExtras * tarifaDeExtras
#                 print ("Tu salario es $ {:.0f} Pesos".format(salario))  
#                 break

#         except ValueError :
#             print ("Valor incorrecto vuelva a intentarlo!!")
#             break

# calcularSalario(240,4166,4731)

largest_so_far = -1
print('Antes', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
        print(largest_so_far, the_num)
print('Después', largest_so_far)

