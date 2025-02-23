import json

class Peliculas:
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.peliculas = json.load(file)
