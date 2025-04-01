import sys
from PySide6.QtWidgets import QApplication
from peliculas import Pelicula
from ventanas import MainWindow
from buscador import BuscadorPeliculas

if __name__ == "__main__":
    app = QApplication(sys.argv)
    modelo = Pelicula('portadas/peliculas.json')
    vista = MainWindow()
    controlador = BuscadorPeliculas(modelo, vista)
    vista.show()
    sys.exit(app.exec())