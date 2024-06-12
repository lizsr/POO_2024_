"""Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente:
a-recorrer la lista y mostrarla
b-hacer una funcion que recorra la lista de numeros y devuelva un string 
c-ordenarla y mostrarla 
d-mostrar su longitud
e-buscar un elemento que el usuario pida por teclado 
"""
def recorrer_lista(mi_lista):
    for numero in mi_lista:
        print(numero, end=" ")

def lista_string(lista):
    return " ".join(map(str, lista))

def ordenar_lista(lista):
    lista.sort()
    return lista 

def longitud_lista(lista):
    return len(lista)

def buscar_elemento(lista, elemento):
    if elemento in lista:
        return f"El elemento {elemento}  si se encuentra  en la lista."
    else:
        return f"El elemento {elemento} no está en la lista,vuelva a intentarlo."


mi_lista = [10, 40, 8, 4, 28, 48, 12, 20]


print("Lista original:")
recorrer_lista(mi_lista)