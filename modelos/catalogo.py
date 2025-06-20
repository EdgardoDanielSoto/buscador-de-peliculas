import json
import os


class Catalogo:
    def __init__(self):
        self.__peliculas = []
        self.__actores = []

    def agregar_pelicula(self, pelicula):
        self.__peliculas.append(pelicula)

    def obtener_peliculas(self):
        return self.__peliculas


    def obtener_contenido_del_archivo(self):
        ruta_archivo = os.path.join("recursos", "peliculas.json")
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except Exception as error:
            print(f"Ocurrió un error: {error}")

    def obtener_actores_unicos(self):
        actores = []
        for pelicula in self.__peliculas:
            for actor in pelicula.obtener_atributos()['Actores']:
                actores.append(actor)
        return sorted(set(actores))


    def buscar_peliculas_por_titulo(self, titulo):
        peliculas_encontradas = []
        for pelicula in self.__peliculas:
            if titulo.lower() in pelicula.obtener_atributos()['Titulo'].lower():
                peliculas_encontradas.append(pelicula)
        return peliculas_encontradas

    def buscar_peliculas_por_actores(self, actor_n1, actor_n2):
        peliculas_encontradas = []
        for pelicula in self.__peliculas:
            actores_minuscula = [actor.lower() for actor in pelicula.obtener_atributos()['Actores']]
            if actor_n1.lower() in actores_minuscula and actor_n2.lower() in actores_minuscula:
                peliculas_encontradas.append(pelicula)
        return peliculas_encontradas



