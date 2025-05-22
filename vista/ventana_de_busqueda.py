from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from ui.ventana_principal import Ui_Ventana_Principal
from PySide6.QtWidgets import QCompleter


class VentanaPrincipal(QWidget):
    buscar = Signal(str)
    abrir_pelicula = Signal(str)
    buscar_pelicula_actores = Signal(str, str)

    def __init__(self, catalogo):
        super(VentanaPrincipal,self).__init__()
        self.__catalogo = catalogo
        self.__ui = Ui_Ventana_Principal()

        self.__ui.setupUi(self)
        self.setWindowTitle("Ventana principal")

        self.__actores_unicos = self.__catalogo.obtener_actores_unicos()
        self.__ui.texto_nombre_primer_actor.setCompleter(QCompleter(self.__actores_unicos, self))
        self.__ui.texto_nombre_segundo_actor.setCompleter(QCompleter(self.__actores_unicos, self))

        self.__titulos_peliculas = [pelicula.obtener_atributos()['Titulo'] for pelicula in self.__catalogo.obtener_peliculas()]
        self.__ui.texto_busqueda_pelicula.setCompleter(QCompleter(self.__titulos_peliculas, self))

        self.__ui.table_peliculas.setRowCount(0)
        self.__ui.table_peliculas.setColumnCount(1)
        self.__ui.table_peliculas.setHorizontalHeaderLabels(["Películas"])
        self.__ui.table_peliculas.verticalHeader().setVisible(False)
        self.__ui.table_peliculas.horizontalHeader().setStretchLastSection(True)
        self.__ui.table_peliculas.itemDoubleClicked.connect(self.emitir_abrir_pelicula)
        self.__ui.boton_buscar_pelicula.setCheckable(True)

    def pelicula_por_titulo(self):
        titulo = self.__ui.texto_busqueda_pelicula.text().lower()
        self.buscar.emit(titulo)

    def emitir_abrir_pelicula(self, item):
        self.abrir_pelicula.emit(item.text())

    def __obtener_nombres_actores(self):
        actor_1 = self.__ui.texto_nombre_primer_actor.text().strip().lower()
        actor_2 = self.__ui.texto_nombre_segundo_actor.text().strip().lower()
        return actor_1, actor_2

    def pelicula_por_actores(self):
        actor_1, actor_2 = self.__obtener_nombres_actores()
        self.buscar_pelicula_actores.emit(actor_1, actor_2)

    def cargar_peliculas(self, peliculas):
        self.__peliculas = []
        self.__completar_tabla(peliculas)

    def __completar_tabla(self, peliculas):
        self.__ui.table_peliculas.setRowCount(0)

        for pelicula in peliculas:
            fila = self.__ui.table_peliculas.rowCount()
            self.__ui.table_peliculas.insertRow(fila)
            self.__ui.table_peliculas.setItem(fila, 0, QTableWidgetItem(pelicula.obtener_atributos()['Titulo']))
            self.__peliculas.append(pelicula)

    def mostrar_error(self, error):
        QMessageBox.warning(self, "Error", error)




