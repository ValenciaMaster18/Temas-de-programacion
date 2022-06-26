class Restaurante:
    
    def __init__(self,nombre,categoria,precio):
        self.nombre = nombre  # 'ATRIBUTOS'
        self.categoria = categoria
        self.precio = precio # "Defaul : public", 'PROTECT': Se puede modificar solo en la clase 
                               # "Private: Solo se puede ver valores y modificar mediante metodos"
    def __str__(self):
        return f"Nombre: \n{self.nombre}. \nCategoria: \n{self.categoria}.\nPrecio: \n{self.precio}"
                               
    # El get se usa para ver el valor cuando esta en private __
    def get_precio(self): 
        return self.precio
    
    # El set se usa para modificar el valor cuando esta en  private __   
    def set_precio(self,precio):
        self.precio  = precio
    
    def mostrarValores (self):
        return f"El nombre del producto es '{self.nombre}' la categoria '{self.categoria}' con un precio de '{self.precio}'"
    
# Instanciar la clase
restaurante = Restaurante ("pescado","carne",25000)
restaurante.set_precio (35000)
precio = restaurante.get_precio ()
print (precio)
print(restaurante)
print(restaurante.mostrarValores())
# Instanciar la clase
restaurante2 = Restaurante ("Lomo","carne",15000)
print (restaurante2)
print(restaurante.mostrarValores())


