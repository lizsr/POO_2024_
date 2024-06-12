peliculas = []

def espereTecla():
    print("Oprima cualquier tecla para continuar ...")
    input()

def insertarPeliculas():
    pelicula = input("Ingrese el nombre de la película: ")
    peliculas.append(pelicula)
    espereTecla()

def eliminarPeliculas():
    nombre = input("Ingresa el nombre de la película a eliminar: ")
    if nombre in peliculas:
        peliculas.remove(nombre)
        print(f"La película '{nombre}' ha sido eliminada.")
        espereTecla()
    else:
        print(f"La película '{nombre}' no se encontró en la lista.")

def consultarpeliculas():
    print("Lista de películas:")
    for pelicula in peliculas:
        print(pelicula)
        espereTecla()

def actualizarPeliculas():
    pelicula_actual = input("Ingrese el nombre de la película a actualizar: ")
    if pelicula_actual in peliculas:
        nuevo_nombre = input("Ingrese el nuevo nombre de la película: ")
        index = peliculas.index(pelicula_actual)
        peliculas[index] = nuevo_nombre
        print(f"La película '{pelicula_actual}' ha sido actualizada a '{nuevo_nombre}'.")
        espereTecla()
    else:
        print(f"La película '{pelicula_actual}' no está en la lista.")

def buscarPeliculas():
    pelicula = input("Ingrese el nombre de la película a buscar: ")
    if pelicula in peliculas:
        index = peliculas.index(pelicula)
        print(f"La película '{pelicula}' está en la posición {index + 1}.")
        espereTecla()
    else:
        print(f"La película '{pelicula}' no está en la lista.")

def vaciarpeliculas():
    peliculas.clear()

import os

from funciones_compartidas import *



while True:
    print("\n\t..::: CINE :::...\n 1.- Agregar\n 2.- Eliminar\n 3.- Consultar\n 4.- Actualizar\n 5.- Buscar\n 6.- Vaciar \n 7.- SALIR ")
    opcion = input("\t Elige una opción: ").upper()

    if opcion == "1" or opcion == "AGREGAR":
        insertarPeliculas()
    elif opcion == "2" or opcion == "ELIMINAR":
        eliminarPeliculas()
    elif opcion == "3" or opcion == "CONSULTAR":
        consultarpeliculas()
    elif opcion == "4" or opcion == "ACTUALIZAR":
        actualizarPeliculas()
    elif opcion == "5" or opcion == "BUSCAR":
        buscarPeliculas()
    elif opcion == "6" or opcion == "VACIAR":
        buscarPeliculas()
    
    elif opcion == "7" or opcion == "SALIR":
        print("Gracias por utilizar el sistema.")
        break
    else:
        print("Opción inválida. Inténtalo nuevamente.")