#programa que solicite nombre del paciente, tipo de sangre, tres mediciones parciales de presion arteria cada 5 minutos_sistolica y diastolica 
#y una medicion final  
#el programa debera solicitar la informacion N veces siempre y cuando la respuesta a la siguiente pregunta sea  "si"
#¿Deseas otra captura?
#se debera imprimir en pantalla el promedio de las presiones arteriales, tambien se debera imprimir en pantalla la presion arterial final que se obtiene del promedio de las presiones y la medicion final, asi como una leyenda que diga: 
#"presenta una presion normal", dependiendo si la presion sistolica es menor o menor a 120 asi como la presion diastolica es menor o igual a 80 
# y por ultimo calcular e imprimir cuantos pacientes fueron capturados


# Programa para capturar datos de pacientes y calcular presiones arteriales


pacientes_capturados = 0
suma_sistolica = 0
suma_diastolica = 0

while True:
    
    nombre = input("Nombre del paciente: ")
    tipo_sangre = input("Tipo de sangre: ")

    
    for i in range(3):
        print(f"Medición {i+1}:")
        Systolica = float(input("Ingrese la presión sistólica del paciente: "))
        DIAstolica = float(input("Ingrese la presión diastólica del paciente: "))
        suma_sistolica += Systolica
        suma_diastolica += DIAstolica

    
    Systolica_final = float(input("Ingresa la presión arterial sistólica final: "))
    DIAstolica_final = float(input("Ingresa la presión arterial diastólica final: "))

    
    promedio_sistolica = suma_sistolica / 3
    promedio_diastolica = suma_diastolica / 3

   
    print(f"Promedio de presión sistólica: {promedio_sistolica:.2f}")
    print(f"Promedio de presión diastólica: {promedio_diastolica:.2f}")

    
    presion_final = (Systolica_final + DIAstolica_final) / 2

   
    if Systolica_final < 120 and DIAstolica_final <= 80:
        print("El paciente presenta una presión normal.")
    else:
        print("El paciente no presenta una presión normal.")

    
    pacientes_capturados += 1

    
    respuesta = input("¿Deseas otra captura? (si/no): ")
    if respuesta.lower() != "si":
        break


print(f"Total de pacientes capturados: {pacientes_capturados}")




