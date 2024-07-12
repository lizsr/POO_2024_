

import os

from funciones_compartidas import *



  


opcion=True
while opcion:
    os.system("clear")
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.-Multiplicacion \n 4.- División \n 5.- Potencia \n 6.-Raiz \n 7.-SALIR ")
    opcion=input("\t Elige una opción: ").upper()
    if opcion!="7":
     n1,n2=solicitarNumeros()
     print(calculadora(n1,n2,opcion))
     espereTecla()

    else:
      opcion=False
      print("Gracias por utilizar el sistema ...")  
