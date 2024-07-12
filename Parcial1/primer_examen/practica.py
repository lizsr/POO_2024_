#Calcular recibo de luz de cfe 
Basico=0.978
Intermedio=1.203
Impuesto=12.56

consumo=int(input("Ingrese la cantidad de kWh que consume: "))


if consumo > 1 and consumo < 150:
  consumo_iva= consumo* 0.16  
  total_pagar= (Basico+consumo_iva)+ Impuesto 
else:
  
   n = consumo - 150 #add
   n1 = Intermedio * n #add
   consumo_iva= n1*0.16  #cambiar consumo -> n1
   total_pagar=n1+consumo_iva+ Impuesto

print(f"El total a pagar es: ${total_pagar: }") 