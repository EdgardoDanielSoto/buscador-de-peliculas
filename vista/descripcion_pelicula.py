from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QPixmap
from ui.segunda_ventana import Ui_SegundaVentana


class VentanaPelicula(QDialog):
    def __init__(self):
        super().__init__()
        self.__ui = Ui_SegundaVentana()
        self.__ui.setupUi(self)
        self.setWindowTitle("Detalles de la Película")

    def mostrar_datos(self, pelicula):
        #self.__ui.label_titulo_ingresado.setText(pelicula.obtener_atributos()["Titulo"])
        self.__ui.texto_sinopsis.setText(pelicula.obtener_atributos()["Sinopsis"])
        #self.__ui.texto_sinopsis.setFixedSize(341, 156)  # Establecer tamaño fijo
        self.__ui.texto_sinopsis.setWordWrap(True)  # Permitir ajuste de texto
        self.__ui.texto_sinopsis.setStyleSheet("QLabel { font-size: 15px; }")  # Ajusta el tamaño de la fuente

        self.__ui.puntuacion.setText(str(pelicula.obtener_atributos()["Puntuacion"]))
        self.__ui.nombres_actores.setText(", ".join(pelicula.obtener_atributos()['Actores']))
        self.__ui.nombres_actores.setWordWrap(True)
        self.__ui.nombres_actores.setStyleSheet("QLabel { font-size: 15px; }")
        ruta = pelicula.cargar_imagen()
        self.__cargar_poster(ruta)

    def __cargar_poster(self, ruta):
        pixmap = QPixmap(ruta)
        if pixmap:
            self.__ui.imagen_descripcion.setPixmap(pixmap.scaled(180, 280))
        else:
            print("Error al cargar la imagen: poster no encontrado.")
