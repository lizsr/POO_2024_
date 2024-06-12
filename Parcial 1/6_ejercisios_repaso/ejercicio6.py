#Mostrar todas las tablas del 1 al 10 
#Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10


for numero in range(1, 11):
    print(f"Tabla del {numero}:")
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")
        
    print()  
