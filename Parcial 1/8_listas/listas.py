"""#list (Array)
#son colecciones o conjunto de datos/valores bajo un ismo nombre,
#para acceder a los valores-se hace con un indice numero

#NOTA: sus valores si son modificados 

#Las listas en una coleccion ordenada y modificable. Permite miembros duplicados.
"""

#Ejemplo 1 crear una lista con valores numericos enteros e imprimir la lista


numeros=(23,24)
print(numeros)

#Recorrer la lista con un for- guada el contenido 

#for i in numeros: 
  #print(i)

#Recorrer la lista con un while- guarda la posicion 

#i=0
#while i <len(numeros):
  # print(numeros[i] )
   #i+=1

#Ejemplo 2 crear una lista de palabras, posteriormente ingresar una palabra para buscar 
#la coincidencia en la lista e indicar si aparece la palabra y en que posicion 
#en caso contrario indicar solo una vez si no la encontro
#semaforo= true-false

#palabras=("hola","2024","10.23", "True")
#print(palabras)

#palabra_buscar=input("Ingresa la palabra a buscar: ")

#noencontro=True
#for i in palabras:
#if palabra_buscar==i:
      #print(f"Encontre la palabra {palabra_buscar}, en la posicion {palabras.index(i)} ") #Index-¿para que sirve?
      #noencontro=False

#if noencontro:
   #print(f"No se encontro la palabra dentro de la lista")


#While


        


#Ejemplo 3  Lista multilinea o multidimensional(matriz ) para crear una agenda telefonica


#agenda=[
  # ["Carlos", 6181234567],
   #["Fernando", 6182334567],
  # ["Matias", 6691112233],
   #["Juan Polainas", 6182332345]
#]

#print(agenda)


#for i in agenda:
  # print(f"{agenda.index(i)+1},-{i}")



#Ejemplo 4 crear un programa que permita gestionar (Administrar) peliculas,  colocar un menu de opciones 
#para agregar remover , consultar peliculas
#NOTAS:
#1. Utilizar funciones y mandar llamar desde otro archivo
#2.Utilizar listas para almacenar los nombres de peliculas

import os

from funciones_de_listas import *

while True:
    print("\n\t..::: CINE :::...\n 1.- Agregar\n 2.- Eliminar\n 3.- Consultar\n 4.- Actualizar\n 5.- Buscar\n 6.- Salir")
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
    elif opcion == "6" or opcion == "SALIR":
        print("Gracias por utilizar el sistema.")
        break
    else:
        print("Opción inválida. Inténtalo nuevamente.")








   