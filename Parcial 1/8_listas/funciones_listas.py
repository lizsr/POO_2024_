#Las tres son unidimencionales
#Son de diferente tipo
#
paises=["Mexico","USA","Brasil", "China"]
numeros=[100,80,3.1416,75]
varios=["UTD",True, 100,0.100]



#Ordenar las listas
print(paises)
paises.sort()#No requiere de parametros, solo logicos,,numeros
print(paises)

print(numeros)
numeros.sort()
print(numeros)

#print(varios)
#varios.sort()
#print(varios)

#Agregar elementos
print(numeros)
numeros.happend(100)
print(numeros)
numeros.inser[len(numeros),200]#Para regresar el tamaño de un arreglo
print(numeros)

#Remover elementos
print(numeros)
numeros.remove(100)
print(numeros)
numeros.pop(5)#trabaja con la pocision
print(numeros)



#Dar vuelta a los elementos
print(varios)
varios.reverse()
print(varios)


#Buscar un valor dentro de una lista

encontro="Brasil" in paises
print (encontro)


#Vaciar una lista 
print(paises)
paises.clear()
print(paises)

#Unir listas

print(varios)
varios.extend(numeros)
print(varios)







