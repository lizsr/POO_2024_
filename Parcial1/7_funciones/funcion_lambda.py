#Funciones lambda son funciones anonimas ya que sirven para abreviar funciones normales
#y normalmente se usan para ejecutar una sola accion

"""

sintaxis:
lambda argumentos_ expresion

Funciones lambda se pueden convertir en funciones normales pero No viceversa
"""
#Ejemplo 1
def suma(n1,n2):
    return n1 +n2
print(suma(8,3))

suma=lambda n1, n2: n1+ n2
print(suma(10,2))

#Ejemplo 2
elevar=lambda numero:numero*numero
print(elevar(3))

#Ejemplo 3
def mensaje():
    nombre=input("Ingrese su nombre por favor")
    return f"Hola,{nombre}!Eres la mejor"
print(mensaje())

mensaje=lambda: f"Hola,{input("Ingrese su nombre por favor")}!Eres la mejor"
print(mensaje())