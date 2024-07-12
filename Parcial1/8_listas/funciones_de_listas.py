

peliculas = []
def espereTecla():
    print("Oprima cualquier tecla para continuar ...")
    input()

def insertarPeliculas():
    pelicula = input("Ingrese el nombre de la película: ")
    peliculas.append(pelicula)
    espereTecla()

def eliminarPeliculas():
    nombre = input("Ingresa el nombre de la película a eliminar: ")
    if nombre in peliculas:
        peliculas.remove(nombre)
        print(f"La película '{nombre}' ha sido eliminada.")
        espereTecla()
    else:
        print(f"La película '{nombre}' no se encontró en la lista.")

def consultarpeliculas():
    print("Lista de películas:")
    for pelicula in peliculas:
        print(pelicula)
        espereTecla()

def actualizarPeliculas():
    pelicula_actual = input("Ingrese el nombre de la película a actualizar: ")
    if pelicula_actual in peliculas:
        nuevo_nombre = input("Ingrese el nuevo nombre de la película: ")
        index = peliculas.index(pelicula_actual)
        peliculas[index] = nuevo_nombre
        print(f"La película '{pelicula_actual}' ha sido actualizada a '{nuevo_nombre}'.")
        espereTecla()
    else:
        print(f"La película '{pelicula_actual}' no está en la lista.")

def buscarPeliculas():
    pelicula = input("Ingrese el nombre de la película a buscar: ")
    if pelicula in peliculas:
        index = peliculas.index(pelicula)
        print(f"La película '{pelicula}' está en la posición {index + 1}.")
        espereTecla()
    else:
        print(f"La película '{pelicula}' no está en la lista.")