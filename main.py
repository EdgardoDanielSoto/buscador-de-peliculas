import sys
from PySide6.QtWidgets import QApplication
from listado_peliculas import Peliculas
from ventanas import MainWindow
from buscador import BuscadorPeliculas

if __name__ == "__main__":
    app = QApplication(sys.argv)
    modelo = Peliculas('portadas/peliculas.json')
    vista = MainWindow()
    controlador = BuscadorPeliculas(modelo, vista)
    vista.show()
    sys.exit(app.exec())