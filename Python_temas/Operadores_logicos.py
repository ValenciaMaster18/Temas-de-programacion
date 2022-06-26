# Operadore logicos:
"""
Los operadores logicos siempre al implementarnos nos devolveran un resultado "bool"

"""
"""
Python tiene 3 operadores logicos:
and  = Los and comparan si ambos condiciones son True.
sino alguna condicion es False, devuelve como resultado False. 

or   = Los or son similares al operador and. Este comprueba, multiples condiciones.
Pero vuelve True si una o ambas condiciones son: True.
 Los or son solo dan un resultado en false ambas condiciones son false

not  = El operador not se aplica a una condicion. Y revierte el resultado de esa condicion.
si es True se convierte a False y si es False se convierte a True.

Resumen:

Utilizar operadores logiocos para combinar varias condicones
Python tiene 3 operadores logicos: not, and, or.
La prioriadad de los operadores va de mayor a menor = not, and y  or.

Interpretacion:

not: funcion logica (no)
and: funcion logica (y)
or: funcion logica (o)

Orden de evaluación de operadores lógicos:

En el caso de varios operadores, Python siempre evalúa la expresión de izquierda a derecha.
Esto se puede verificar con el siguiente ejemplo.

"""
# Operador logico and:
# Ejemplo 1:
"""
a = 10
b = 10
c = -10
  
if a > 0 and b > 0: 
    print("Los números son mayores que 0") 
  
if a > 0 and b > 0 and c > 0: 
    print("Los números son mayores que 0") 
else: 
    print("Al menos un número no es mayor que 0") 


# Ejemplo 2:

a = 10
b = 12
c = 0
  
if a and b and c: 
    print("Todos los números tienen valor booleano como True") 
else: 
    print("Al menos un número tiene valor booleano como False")

# Operadore logico or:
# Ejemplo 1:

a = 10
b = -10
c = 0
  
if a > 0 or b > 0: 
    print("Cualquiera de los números es mayor que 0") 
else: 
    print("Ningún número es mayor que 0") 
  
if b > 0 or c > 0: 
    print("Cualquiera de los números es mayor que 0") 
else: 
    print("Ningún número es mayor que 0") 

# Ejemplo 2:

a = 10
b = 12
c = 0
  
if a or b or c: 
    print("Al menos un número tiene valor booleano como True") 
else: 
    print("Todos los números tienen valor booleano como False") 

# Operadores logicos not:
# Ejemplo 1:

  
a = 10
  
if not a: 
    print("El valor booleano de a es True") 
  
if not (a%3 == 0 or a%5 == 0): 
    print("10 no es divisible por 3 o 5") 
else: 
    print("10 es divisible por 3 o 5") 
"""
# Orden de evaluacion de operadores logicos:
# Ejemplo 

def orden(x): 
    print("Método llamado para valor: ", x) 
    return True if x > 0 else False
      
a = orden
b = orden
c = orden
  
if a(-1) or b(5) or c(10): 
    print("Al menos uno de los números es positivo")