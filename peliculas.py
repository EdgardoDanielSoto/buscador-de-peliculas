import json

class Pelicula:
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.pelicula = json.load(file)

class Catalogo:
    def __init__(self):
        self.__catalogo = []

    def agregar_pelicula(self, pelicula):
        self.__catalogo.append(pelicula)

    def obtener_peliculas(self):
        return self.__catalogo