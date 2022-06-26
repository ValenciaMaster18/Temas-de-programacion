print("Evaluacion de sistema electrico")

num_subs = input("Introducir su nombre: ")
num_contrat = int(input("Introducir numero de contrato '4 Digitos': " ))
tipo_de_suscriptor = int(input("""Introducir tipo de suscritor: \nresidencial (1) o comercial (2): """))
lec_inicial = int(input("Introducir la lectura inicial electrica en Kwh: "))
lec_final = int(input("Introducir la lectura final electrica en Kwh: "))

def electric (num_contrat,tipo_de_suscriptor,lec_inicial,lec_final):
	if (num_contrat >1000) and (tipo_de_suscriptor == "1"
	if