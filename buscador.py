import sys
import random
from PySide6.QtWidgets import QApplication, QCompleter
from PySide6.QtCore import Qt
from listado_peliculas import ListaPeliculas
from ventanas import MainWindow, SegundaVentana

class BuscadorPeliculas:
    def __init__(self, modelo, vista):
        self.__model = modelo
        self.__view = vista
        self.__peliculas = self.__model.get_peliculas()
        self.__peliculas_mostradas = []

        titulos_peliculas = [p['titulo'] for p in self.__peliculas]
        self.__view._MainWindow__ui.texto_busqueda_pelicula.setCompleter(QCompleter(titulos_peliculas, self.__view))
        self.__view._MainWindow__ui.texto_busqueda_pelicula.completer().setCaseSensitivity(Qt.CaseInsensitive)

        actores = set(actor for pelicula in self.__peliculas for actor in pelicula['actores'])
        completer_actores = QCompleter(list(actores), self.__view)
        completer_actores.setCaseSensitivity(Qt.CaseInsensitive)
        self.__view._MainWindow__ui.texto_nombre_primer_actor.setCompleter(completer_actores)
        self.__view._MainWindow__ui.texto_nombre_segundo_actor.setCompleter(completer_actores)

        self.__view._MainWindow__ui.boton_buscar_pelicula.clicked.connect(self.__buscar_por_titulo)
        self.__view._MainWindow__ui.boton_buscar_actores.clicked.connect(self.__buscar_por_actores)

        self.__frames = [
            ('imagen_pelicula_uno', 'boton_nombre_pelicula_uno'),
            ('imagen_pelicula_dos', 'boton_nombre_pelicula_dos'),
            ('imagen_pelicula_tres', 'boton_nombre_pelicula_tres'),
            ('imagen_pelicula_cuatro', 'boton_nombre_pelicula_cuatro'),
            ('imagen_pelicula_cinco', 'boton_nombre_pelicula_cinco'),
            ('imagen_pelicula_seis', 'boton_nombre_pelicula_seis'),
            ('imagen_pelicula_siete', 'boton_nombre_pelicula_siete'),
            ('imagen_pelicula_ocho', 'boton_nombre_pelicula_ocho'),
            ('imagen_pelicula_nueve', 'boton_nombre_pelicula_nueve'),
            ('imagen_pelicula_diez', 'boton_nombre_pelicula_diez')
        ]

        self.__mostrar_todas_peliculas()

    def __abrir_segunda_ventana(self, index):
        if index < len(self.__peliculas_mostradas):
            pelicula = self.__peliculas_mostradas[index]
            ventana_informacion = SegundaVentana(pelicula, self.__view)
            ventana_informacion.exec()

    def __mostrar_todas_peliculas(self):
        random.shuffle(self.__peliculas)
        self.__peliculas_mostradas = self.__peliculas[:10]

        for i, (label, boton) in enumerate(self.__frames):
            label_widget = getattr(self.__view._MainWindow__ui, label)
            boton_widget = getattr(self.__view._MainWindow__ui, boton)
            pelicula = self.__peliculas_mostradas[i]

            self.__view.set_pelicula_info(label_widget, pelicula)
            label_widget.setVisible(True)
            boton_widget.setVisible(True)
            boton_widget.setText(pelicula['titulo'])
            try:
                boton_widget.clicked.disconnect()
            except TypeError:
                pass
            boton_widget.clicked.connect(lambda _, idx=i: self.__abrir_segunda_ventana(idx))

    def __buscar_por_titulo(self):
        nombre_buscado = self.__view._MainWindow__ui.texto_busqueda_pelicula.text().strip().lower()

        if not nombre_buscado:
            self.__mostrar_todas_peliculas()
            return

        resultados = [pelicula for pelicula in self.__peliculas if nombre_buscado in pelicula['titulo'].strip().lower()]

        if resultados:
            resultados.sort(key=lambda pelicula: pelicula['titulo'])
            self.__mostrar_resultados(resultados)
        else:
            self.__view.mostrar_alerta("Película no encontrada")

    def __buscar_por_actores(self):
        actor_uno_buscado = self.__view._MainWindow__ui.texto_nombre_primer_actor.text().strip().lower()
        actor_dos_buscado = self.__view._MainWindow__ui.texto_nombre_segundo_actor.text().strip().lower()

        if not actor_uno_buscado or not actor_dos_buscado:
            self.__view.mostrar_alerta("Debe ingresar los nombres de dos actores")
            return

        resultados = []
        for pelicula in self.__peliculas:
            actor_uno_coincide = any(actor_uno_buscado in actor.strip().lower() for actor in pelicula['actores'])
            actor_dos_coincide = any(actor_dos_buscado in actor.strip().lower() for actor in pelicula['actores'])

            if actor_uno_coincide and actor_dos_coincide:
                resultados.append(pelicula)

        if resultados:
            resultados.sort(key=lambda pelicula: pelicula['titulo'])
            self.__mostrar_resultados(resultados)
        else:
            self.__view.mostrar_alerta("Película no encontrada")

    def __mostrar_resultados(self, resultados):
        self.__peliculas_mostradas = resultados[:10]

        for i, (label, boton) in enumerate(self.__frames):
            label_widget = getattr(self.__view._MainWindow__ui, label)
            boton_widget = getattr(self.__view._MainWindow__ui, boton)

            if i < len(self.__peliculas_mostradas):
                pelicula = self.__peliculas_mostradas[i]
                self.__view.set_pelicula_info(label_widget, pelicula)
                label_widget.setVisible(True)
                boton_widget.setVisible(True)
                boton_widget.setText(pelicula['titulo'])
                try:
                    boton_widget.clicked.disconnect()
                except TypeError:
                    pass
                boton_widget.clicked.connect(lambda _, idx=i: self.__abrir_segunda_ventana(idx))
            else:
                label_widget.setVisible(False)
                boton_widget.setVisible(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    modelo = ListaPeliculas('portadas/peliculas.json')
    vista = MainWindow()
    controlador = BuscadorPeliculas(modelo, vista)
    vista.show()
    sys.exit(app.exec())