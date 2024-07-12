from conexionBD import*

try:
    micursor=conexion.cursor()
    sql="update cliente  set direccion='col. del UTD' where  id=1" 


    micursor.execute(sql)
    #Es necesario ejecutar el commit para que finalice el SQL con exito
    conexion.commit()
except:
    print(f"Ocurrio un error por favor vuelva a intentar mas tarde")

else:
    print("Registro Actualizado con exito")