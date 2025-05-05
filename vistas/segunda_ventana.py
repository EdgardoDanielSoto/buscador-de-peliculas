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

