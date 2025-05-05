import json

class Catalogo:
    def __init__(self, file_path):
        self.__catalogo = []
        self.__cargar_peliculas(file_path)

    def __cargar_peliculas(self, file_path):

        with open(file_path, 'r') as file:
            self.__catalogo = json.load(file)

    def __obtener_peliculas(self):
        return self.__catalogo

    def __buscar_por_titulo(self, titulo):
        return [pelicula for pelicula in self.__catalogo if titulo.lower() in pelicula['titulo'].lower()]

    def __buscar_por_actor(self, actor):
        return [pelicula for pelicula in self.__catalogo if any(actor.lower() in a.lower() for a in pelicula['actores'])]
