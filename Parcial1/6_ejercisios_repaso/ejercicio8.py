#Hacer un programa que resuelva lo siguiente ¿Cuanto es el x por ciento de x numero ?



porcentaje = float(input("Ingresa el porcentaje: "))
numero = float(input("Ingresa el número a sacar el porcentaje: "))


resultado = (porcentaje / 100) * numero


print(f"{porcentaje}% de {numero} es igual a {resultado: }")


