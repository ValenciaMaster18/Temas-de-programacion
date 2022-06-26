# Calculadora IMC
# IMC = Peso (Altura x Altura)
# < 19: Delgadez
# Entre 20 y 25: Normal
# Entre 26 y 30: Sobrepeso
# > de 30: Obesidad

def calcularIMC(Peso, alturaEnMetros):
    imc = Peso / (alturaEnMetros * alturaEnMetros)
    return imc


def pedirELIMC():
    peso = float(input("Introduce tu peso en kg: "))
    alturaEnCM= int(input("Introduce tu altura en cm: "))
    alturaEnMetros = alturaEnCM / 100
    imc = calcularIMC(peso, alturaEnMetros)

    print("Su IMC es de " + str(imc))

    if imc < 20:
        print("Estado de delgadez")
    elif imc >= 20 and imc <26:
        print("Peso normal")
    elif imc >=26 and imc <30:
        print("Estado de sobrepeso")
    else:
        print("Estado de obesidad")


print("Calcular el IMC de Luis valencia")
pedirELIMC( )