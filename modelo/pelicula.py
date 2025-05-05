import json
import os


file_path = os.path.join('portadas', 'peliculas.json')

with open(file_path, 'r') as file:
    peliculas = json.load(file)


for pelicula in peliculas:
    if pelicula['titulo'] == "La historia oficial":
        print("Datos de la película:")
        print(f"Título: {pelicula['titulo']}")
        print(f"Actores: {', '.join(pelicula['actores'])}")
        print(f"Sinopsis: {pelicula['sinopsis']}")
        print(f"País: {pelicula['pais']}")
        print(f"Imagen: {pelicula['imagen']}")
        print(f"Puntuación: {pelicula['Puntuacion']}")
        print(f"Género: {pelicula['Genero']}")
        break
