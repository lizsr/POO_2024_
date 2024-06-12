#Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los primeros 60 numeros reales
#Resolverlo con while y for 
#


#while
numero = 1
while numero <= 60: 
    cuadrado = numero ** 2
    print(f"El cuadrado del {numero} es {cuadrado}")
    numero +=1




#for
for numero in range(1, 61): 
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es {cuadrado}")
