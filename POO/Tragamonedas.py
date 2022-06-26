from random import randint

class Tragamoneda:
    def __init__(self, id , premio):
        self.id = id
        self.premio = premio 
        self.moneda = 0
        self.jackpot = 0
    def __str__(self):
        return "El id: " + str(self.id) + " premio: " + str(self.premio)
    
    def __eq__(self, otro):
        return self.monedas == otro.monedas
    
    def __lt__(self, otro):
        return self.monedas < otro.monedas
    
    def __gt__(self, otro):
        return self.monedas > otro.monedas    
    
    def jugar(self):
        self.moneda += 10
        numero = randint(1,9),randint(1,9),randint(1,9)
        mensaje = ""
        if numero[0] == numero[1] == numero[2]:
            mensaje = "Felicidades !! Ganastes"
            self.jackpot += 1
            self.premio *= 2
        else:
            mensaje = "Mejor suerte para la proxima"
        return numero,mensaje

tragamonedas_a = Tragamoneda (1,1000)
tragamonedas_b = Tragamoneda (2,500)

for i in range(150):
    print(tragamonedas_a.jugar())
    print(tragamonedas_b.jugar())
print("El id: ",tragamonedas_a.id," Monedas Gastadas ",tragamonedas_a.moneda," N° de jackpot ",tragamonedas_a.jackpot," Ganacias: ",tragamonedas_a.premio)
print("El id: ",tragamonedas_b.id," Monedas Gastadas ",tragamonedas_b.moneda," N° de jackpot ",tragamonedas_b.jackpot," Ganacias: ",tragamonedas_b.premio)
print("\n",tragamonedas_a,"\n",tragamonedas_b)
        
        
