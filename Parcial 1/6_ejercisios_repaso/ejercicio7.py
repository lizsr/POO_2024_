#Hacer un programa que muestre todos los numeros impares entre 2 numeros que te de el usuario



inicio  = int(input("Puedes ingresar un numero: "))
fin = int(input("Puedes ingresa un segundo numero: "))


if inicio > fin:
    inicio, fin = fin, inicio

print(f"Los números impares  entre {inicio} y {fin} son:")
for numero in range(inicio, fin +1 ):
     if numero % 2 != 0:
       print(numero)

