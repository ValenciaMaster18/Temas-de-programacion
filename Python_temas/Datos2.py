"""
2. Para determinar si se concede a un cliente un préstamo a 20 años, el banco procede a verificar los 
ingresos en pesos anuales del solicitante. 

Silos ingresos son superiores a $20.000.000, el crédito se 
concede
.
Si los ingresos son inferiores a $20.000.000 pero superiores a $12.000.000 y esta soltero el 
crédito se concede.

También se le concede si tiene ingresos entre $20.000.000 y $15.000.000 y está 
casado sin hijos. 

Realizar un programa en Python que pida los ingresos anuales y el estado civil del 
solicitante y si tiene hijos y muestre por pantalla si se le concede el crédito o no.
"""

print ("Proceso de validacion para aplicar a un prestamo en el banco")

ingresos_anuales = int(input("¿Cual es su salario anual? \nRespueta: ")

estado_civil = input("Ustede esta: \nRespuesta: soltero (1) o casado (0): ")


if ingresos_anuales > 20_000_000:
	print("Prestamo Aprobado")

if ingresos_anuales < 20_000_000  ingresos_anuales or > 12_000_000 and estado_civil == 1:
	print("Prestamo Aprobado")

	
