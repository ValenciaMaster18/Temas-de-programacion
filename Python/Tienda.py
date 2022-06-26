# print ("Programa para calcular edades")
# edades = []
# for i in range(1,11):
#     pregunta = int(input("Digite su edad: "))
#     edades.append(pregunta) 
#  print (edades)
#  promedio = sum(edades) / len(edades)
#  print (f"El promedio de las edades es: {promedio}")

print ("Surtidos Thomas77")
name_product = ("Pescado","Pollo","Cerdo","Pechuga","Higado")
price = []
amount = []

while True:
    print ("Menu")
    print ("1. Ver productos")
    print ("2  Ver el total total")
    print ("3. Salir de la tienda")
    respuesta = int(input("Digite una opcion del menu: "))
    if respuesta > 0 or respuesta < 3:
        print ("Opcion del menu incorrecto")

    if respuesta == 1:
        print (name_product)
        to_buy = input("¿Que producto desea comprar?: ").capitalize()
        
        if to_buy == "Pescado":
            prices = float(input("Digite precio del producto: "))
            amounts = float(input("Digite la cantidad del  producto: "))
            cost = prices * amounts
            price.append(cost)
            amount.append(amounts)
  
        elif to_buy == "Pollo":
            prices = float(input("Digite precio del producto: "))
            amounts = float(input("Digite la cantidad del  producto: "))
            cost = prices * amounts
            price.append(cost)
            amount.append(amounts)       

        elif to_buy == "Cerdo":
            prices = float(input("Digite precio del producto: "))
            amounts = float(input("Digite la cantidad del  producto: "))
            cost = prices * amounts
            price.append(cost)
            amount.append(amounts)

        elif to_buy == "Pechuga":
            prices = float(input("Digite precio del producto: "))
            amounts = float(input("Digite la cantidad del  producto: "))
            cost = prices * amounts
            price.append(cost)
            amount.append(amounts)

        elif to_buy == "Higado":
            prices = float(input("Digite precio del producto: "))
            amounts = float(input("Digite la cantidad del  producto: "))
            cost = prices * amounts
            price.append(cost)
            amount.append(amounts)
    if respuesta == 2:
            print (sum(price))
            
    if respuesta == 3:
        break
 
        
if sum(price) > 50000:
    discount = sum(price) * 0.02
    total = sum(price) -  discount 
    print (f"El descuento es del 2% es ${discount:.0f}")
    print (f"Total a pagar menos el descuento es ${total}")
elif sum(price) <= 50000:
    print (f"El total a pagar de su compra es ${sum(price)}")
else:
    if sum(price) <= 0:
        print ("No compro ningun producto")
