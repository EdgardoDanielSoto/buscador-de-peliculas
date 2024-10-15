import os
from PySide6.QtWidgets import QWidget, QDialog, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from ui.ventana_principal import Ui_ventana_principal
from ui.segunda_ventana import Ui_SegundaVentana

class SegundaVentana(QDialog):
    def __init__(self, pelicula, parent=None):
        super(SegundaVentana, self).__init__(parent)
        self.__ui = Ui_SegundaVentana()
        self.__ui.setupUi(self)
        self.setWindowTitle(pelicula['titulo'])

        if 'imagen' in pelicula:
            imagen_path = pelicula['imagen']
            pixmap = QPixmap(imagen_path)
            if not pixmap.isNull():
                self.__ui.imagen_descripcion.setPixmap(pixmap)
            else:
                self.__ui.imagen_descripcion.setText("Imagen no disponible")
        else:
            self.__ui.imagen_descripcion.setText("Imagen no disponible")

        if 'sinopsis' in pelicula:
            self.__ui.texto_sinopsis.setText(pelicula['sinopsis'])
            self.__ui.texto_sinopsis.setWordWrap(True)
        else:
            self.__ui.texto_sinopsis.setText("Sinopsis no disponible")
            self.__ui.texto_sinopsis.setWordWrap(True)

        if 'actores' in pelicula:
            self.__ui.nombres_actores.setText(", ".join(pelicula['actores']))
            self.__ui.nombres_actores.setWordWrap(True)
        else:
            self.__ui.nombres_actores.setText("Actores no disponibles")
            self.__ui.nombres_actores.setWordWrap(True)

        if 'Puntuacion' in pelicula:
            self.__ui.puntuacion.setText(str(pelicula['Puntuacion']))
        else:
            self.__ui.puntuacion.setText("Puntuación no disponible")

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__ui = Ui_ventana_principal()
        self.__ui.setupUi(self)

    def set_pelicula_info(self, label, pelicula):
        if 'imagen' in pelicula:
            imagen_path = os.path.join(os.path.dirname(__file__), pelicula['imagen'])
            if os.path.exists(imagen_path):
                pixmap = QPixmap(imagen_path)
                if not pixmap.isNull():
                    pixmap = pixmap.scaled(label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    label.setPixmap(pixmap)
                else:
                    print(f"Error: No se pudo cargar la imagen desde {imagen_path}")
            else:
                print(f"Error: La ruta de la imagen {imagen_path} no existe")
        else:
            print("Error: La película no tiene una clave 'imagen'")

    def mostrar_alerta(self, mensaje):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Alerta")
        msg_box.setText(mensaje)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()