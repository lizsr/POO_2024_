#Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario



# Numeros ingresados 
inicio = int(input("Ingresa el primer numero: "))
fin = int(input("Ingresa el segundo numero: "))

# Mostrar los números entre el rango
print(f"Los números entre {inicio} y {fin} son:")
for numero in range(inicio, fin +1 ):
    print(numero)

