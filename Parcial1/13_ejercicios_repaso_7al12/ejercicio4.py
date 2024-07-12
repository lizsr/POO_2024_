"""
Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico
y que imprima un mensaje de acuerdo al tipo de dato 
de cada variable. Usar funciones


"""

def tipo_variable(variable):
    if isinstance(variable, list):
        print("La variable es una lista.")
    elif isinstance(variable, str):
        print("La variable es una cadena.")
    elif isinstance(variable, int):
        print("La variable es un entero.")
    elif isinstance(variable, bool):
        print("La variable es un booleano.")
    else:
        print("Tipo de dato desconocido.")

#global los tipos de datos
lista = [1, 2, 3]
cadena = "Hola, mundo"
entero = 42
booleano = True


tipo_variable(lista)
tipo_variable(cadena)
tipo_variable(entero)
tipo_variable(booleano)