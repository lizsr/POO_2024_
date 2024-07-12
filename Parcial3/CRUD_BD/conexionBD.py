import mysql.connector 

#Conexion con la BD de MySQL
try:
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_python'
)
except Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    print(f"Ocurrio un error por favor vuelva a intentar mas tarde ")




#verificar si la conexion es correcta
if conexion.is_connected():
    print("Se creo la conexion exitosamente.")

else:
    print(f"No fue posible conectar con la base de datos")