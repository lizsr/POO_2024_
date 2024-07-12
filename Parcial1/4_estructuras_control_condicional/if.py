#Existe una estructura llmada if la cual evalua una condicion para encontrar el valor "True" y si se cumple la condicion 
#se ejecuta la linea o lineas de codigo

#Tenemos 4 variantes del if

# 1.-if simple
# 2._if compuesto
# 3._if anidado
# 4._if y elif


#Ejemplo: 1.if simple
color=input("Ingresa un color")
if color=="rojo":
    print("Soy el color rojo")


#Ejemplo: 2.if compuesto
color=input("Ingresa un color:")
if color=="rojo":
    print("Soy el color rojo")
else:
    print("No soy el color rojo")    

#Ejemplo: 3.if anidado
color=input("Ingresa un color")

if color=="rojo":
    print("Soy el color rojo")
    if color=="rojo":
         print("No soy el color rojo")  


 #Ejemplo: 4.if y elif
color=input("Ingresa un color:")

if color=="rojo":
    print("Soy el color rojo")
elif color=="amarillo":
    print("Soy el color amarillo") 
elif color=="azul":  
     print("Soy el color azul") 
elif color=="morado": 
    print("Soy el color morado")
else:
     print("No soy ninguno de los colores anteriores")


#Ejemplo 4 Crear un programa que solicite el numero de la semana 
#e imprima en pantalla el dia que le corresponde
  


    
dia=int(input("Ingrese un número del 1 al 7: "))


 

   


