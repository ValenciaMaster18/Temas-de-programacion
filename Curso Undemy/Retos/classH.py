from Restaurante import Restaurante

class Hotel(Restaurante):
    
    def __init__(self,nombre,categoria,precio,piscina):
        super().__init__(nombre,categoria,precio)
        # Estamos añadiendo atributos a nuestra clase hija
        self.piscina = piscina
        # Estamos rescribiendo un metodo (debellamrse igual)
    def mostrarValores(self):
        return f"El nombre del producto es '{self.nombre}' la categoria '{self.categoria}' con un precio de '{self.precio}' tiene piscina '{self.piscina}'"

    def get_piscina(self):
        return self.piscina
    def get_nombre(self):
        return self.nombre
    
hotel = Hotel ("Del prado","Hotel",100000,"si")
print(hotel.mostrarValores())
nombre = hotel.get_nombre()
piscina = hotel.get_piscina()

print (f"El {nombre} tiene piscina {piscina}")