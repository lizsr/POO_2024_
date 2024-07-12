# Una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular
#como un programa mas pequeño que cumple una funcion especifica.
#La funcion se puede reutilizar con el simple hecho de envocarla es decir mandarla llamar 


#Sintaxis :

#def nombredemifuncion (parametros):
    #bloque o cunjunto de instrucciones

#nombredemifuncion   (parametros)

#Las funciones pueden ser de 4 tipos
#- 1 Funcion que no recibe parametros y no regresa valor
#- 2 Funcion que no recibe parametros y regresa valor 
#- 3 Funcion que  recibe parametros y  no regresa valor 
#- 4 Funcion que  recibe parametros y regresa valor 


#- 1 Funcion que no recibe parametros y no regresa valor

def sumaNumero1():
    n1=int(input("numero# 1:"))
    n2=int(input("numero# 2:"))
    suma=n1+n2
    print(f"{n1} +{n2}={suma}")
sumaNumero1()    

#- 2 Funcion que no recibe parametros y regresa valor
def sumaNumero2():
    n1=int(input("numero# 1:"))
    n2=int(input("numero# 2:"))
    suma=n1+n2
    return f"{n1} +{n2}={suma}"
print(sumaNumero2()) 

#- 3 Funcion que  recibe parametros y  no regresa valor "No se puede hacer mas grande(incluir cosas)"
def sumaNumero3(n1,n2):
    suma=n1+n2
    print(f"{n1} +{n2}={suma}")

n1=int(input("numero# 1:"))
n2=int(input("numero# 2:"))
sumaNumero3(n1,n2) 


#- 4 Funcion que  recibe parametros y  regresa valor  -(mas utilizado)-
#"se puede agregar mas contenido,la ultima linea se puede colocar mas abajo "
#No se tiene que pedir nada 
def sumaNumero4(n1,n2):
    suma=n1+n2
    return f"{n1} +{n2}={suma}"

n1=int(input("numero# 1:"))
n2=int(input("numero# 2:"))
print(sumaNumero4()) 


#Crear un programa que solicite a traves de una funcion la siguiente informacion 
#nombre del paciente, edad, estatura, tipo de sangre 
#utilizar los 4 tipos de funciones 


# 1-Función que no recibe parámetros y no regresa valor
def solicitar_informacion():
    print("Ingrese la siguiente información del paciente:")
    nombre = input("Nombre: ")
    edad= input("Edad: ")
    estatura = input("Estatura: ")
    tipo_sangre = input("Tipo de sangre: ")
solicitar_informacion()


# 2-Función que no recibe parámetros y regresa valor
def obtener_informacion():
    return input("Ingrese la información del paciente (nombre, edad, estatura, tipo de sangre): ")
informacion = obtener_informacion()
print("Información ingresada:", informacion)


#3- Función que recibe parámetros y no regresa valor
def mostrar_informacion(nombre, edad, estatura, tipo_sangre):
    print(f"Información del paciente:")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Estatura: {estatura} cm")
    print(f"Tipo de sangre: {tipo_sangre}")
nombre, edad, estatura, tipo_sangre = informacion.split(", ")
mostrar_informacion(nombre, edad, estatura, tipo_sangre)


# 4-Función que recibe parámetros y regresa valor
def formatear_informacion(nombre, edad, estatura, tipo_sangre):
    return f"Nombre: {nombre}, Edad: {edad}, Estatura: {estatura} cm, Tipo de sangre: {tipo_sangre}"
informacion_formateada = formatear_informacion(nombre, edad, estatura, tipo_sangre)
print("Información formateada:", informacion_formateada)



#03/junio/2024







