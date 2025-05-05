import os
from PySide6.QtWidgets import QWidget, QDialog, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from ui.ventana_principal import Ui_ventana_principal
from ui.segunda_ventana import Ui_SegundaVentana



class VentanaPrincipal(QWidget):
    def __init__(self, parent=None):
        super(VentanaPrincipal, self).__init__(parent)
        self.ui = Ui_ventana_principal()
        self.ui.setupUi(self)

        # Connect signals to slots (if needed)
        self.ui.boton_buscar_pelicula.clicked.connect(self.buscar_pelicula)
        self.ui.boton_buscar_actores.clicked.connect(self.buscar_actores)

    def buscar_pelicula(self):
        # Logic for searching a movie
        pelicula = self.ui.texto_busqueda_pelicula.text()
        print(f"Buscando película: {pelicula}")

    def buscar_actores(self):
        # Logic for searching by actors
        actor1 = self.ui.texto_nombre_primer_actor.text()
        actor2 = self.ui.texto_nombre_segundo_actor.text()
        print(f"Buscando actores: {actor1}, {actor2}")

    def mostrar_alerta(self, mensaje):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Alerta")
        msg_box.setText(mensaje)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()