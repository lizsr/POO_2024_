
"""
Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla 
con palabras o frases asta que el usuario asi lo crea conveniente ,
posteriormente imprimir el contenido de la lista en mayusculas

"""


lista = []


def llenado():
 if not lista:
    print(f"La lista está vacía,por favor introduce  palabras o frases para llenarla ")
    

   
    while True:
        entrada = input("Ingresa una palabra o frase: ")
        if entrada.lower() == "salir":
            break
        lista.append(entrada)
    return lista

   
    for elemento in lista:
        print(elemento.upper())
 else:
    print("Se agregaron elementos a la lista")

llenado()