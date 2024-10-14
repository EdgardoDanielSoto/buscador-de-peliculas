import json

class ListaPeliculas:
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.__peliculas = json.load(file)

    def get_peliculas(self):
        return self.__peliculas