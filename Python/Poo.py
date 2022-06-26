class Alumnos:
    # Inicializamos los productos
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print("Alumnos ",self.nombre)
        print("La nota es ",self.nota)
    def resultado(self):
        if self.nota <= 5:
            print("No aprobado")
        else:
            print("Aprobado")
            
Alumno1 = Alumnos("Luis",5)
Alumnos2 = Alumnos("Andrew",10)

Alumno1.imprimir()
Alumno1.resultado()

Alumnos2.imprimir()
Alumnos2.resultado()    
    
from random import randint

class Tragamoneda:
    def __ini__(self, id , premio):
        self.id = id
        self.premio = premio 
        self.moneda = 0
        self.jackpot = 0
    def jugar(self):
        self.moneda += 1
        numero = randint(0,9),randint(0,9,),randint(0,9)
        mensaje = ""
        if numero[0]==numero[1]==numero==[2]:
            mensaje = "Felicidades !! Ganastes"
            self.jackpot += 1
        else:
            mensaje = "Mejor suerte para la proxima"
        return numero,mensaje

tragamonedas_a = Tragamoneda (1,500)
tragamonedas_b = Tragamoneda (2,250)

for i in range(50):
    print(tragamonedas_a.jugar())
    print(tragamonedas_b.jugar())
