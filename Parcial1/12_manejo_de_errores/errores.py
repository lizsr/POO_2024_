#Manejo de errores es la forma en la que tienen los lenguajes de programacion 
#para evitar que sucedan errores en tiempo de ejecucion 

#Ejemplo 1 error cuando una variable no se genera
try:
 nombre=input("Dame el nombre: ")

 if len(nombre)>1:
    nombre_usuario="El nombre es:" +nombre

 print(nombre_usuario)
except:
  print("Es necesario introducir un nombre de ususario...")

#Ejemplo 2 cuando se solicita un numero y se introduce una letra- #ValueError- cuando quiere convertir algo a numero que no sea numero
try:
 numero=int(input("Dame un numero: "))

 if numero>0 :
  print("Soy un numero entero positivo ")
 else:
   print("Soy un numero enteo negativo")
except:
 print("No se puede convertir un caracter numerico a numero ") #puede llamarse funciones,puede llevar un ciclo

else:
  print("Todo es correcto")

#Ejemplo 3 cuando se generan multiples excepciones
try:
 numero=int(input("Dame un  numero: "))

 print("El cuadrado es: " +str(numero*numero))
except ValueError:
  print("Debes introducir un numero, no se puede convertir un caracter(numero) que no sea numerico..")

except TypeError:
  print("No es posible convertir el numero a entero")

else:
  print("Se finalizo correctamente")

finally:
 print("Se termino")
  