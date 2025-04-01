import random

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCompleter

from ventanas import SegundaVentana


class BuscadorPeliculas:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.__vista = vista
        self.pelicula = self.modelo.pelicula
        self.__peliculas_mostradas = []

        titulos_peliculas = [p['titulo'] for p in self.pelicula]
        self.__vista._MainWindow__ui.texto_busqueda_pelicula.setCompleter(QCompleter(titulos_peliculas, self.__vista))
        self.__vista._MainWindow__ui.texto_busqueda_pelicula.completer().setCaseSensitivity(Qt.CaseInsensitive)

        actores = set(actor for pelicula in self.pelicula for actor in pelicula['actores'])
        completer_actores = QCompleter(list(actores), self.__vista)
        completer_actores.setCaseSensitivity(Qt.CaseInsensitive)
        self.__vista._MainWindow__ui.texto_nombre_primer_actor.setCompleter(completer_actores)
        self.__vista._MainWindow__ui.texto_nombre_segundo_actor.setCompleter(completer_actores)

        self.__vista._MainWindow__ui.boton_buscar_pelicula.clicked.connect(self.buscar_por_titulo)
        self.__vista._MainWindow__ui.boton_buscar_actores.clicked.connect(self.buscar_por_actores)

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

        self.mostrar_todas_peliculas()

    def abrir_segunda_ventana(self, index):
        if index < len(self.__peliculas_mostradas):
            pelicula = self.__peliculas_mostradas[index]
            ventana_informacion = SegundaVentana(pelicula, self.__vista)
            ventana_informacion.exec()

    def mostrar_todas_peliculas(self):
        random.shuffle(self.pelicula)
        self.__peliculas_mostradas = self.pelicula[:10]

        for i, (label, boton) in enumerate(self.__frames):
            label_widget = getattr(self.__vista._MainWindow__ui, label)
            boton_widget = getattr(self.__vista._MainWindow__ui, boton)
            pelicula = self.__peliculas_mostradas[i]

            self.__vista.set_pelicula_info(label_widget, pelicula)
            label_widget.setVisible(True)
            boton_widget.setVisible(True)
            boton_widget.setText(pelicula['titulo'])
            boton_widget.clicked.connect(lambda _, idx=i: self.abrir_segunda_ventana(idx))
            try:
                boton_widget.clicked.disconnect()
            except TypeError:
                pass
            boton_widget.clicked.connect(lambda _, idx=i: self.abrir_segunda_ventana(idx))

    def buscar_por_titulo(self):
        nombre_buscado = self.__vista._MainWindow__ui.texto_busqueda_pelicula.text().strip().lower()

        if not nombre_buscado:
            self.mostrar_todas_peliculas()
            return

        resultados = [pelicula for pelicula in self.pelicula if nombre_buscado in pelicula['titulo'].strip().lower()]

        if resultados:
            resultados.sort(key=lambda pelicula: pelicula['titulo'])
            self.mostrar_resultados(resultados)
        else:
            self.__vista.mostrar_alerta("Película no encontrada")

    def buscar_por_actores(self):
        actor_uno_buscado = self.__vista._MainWindow__ui.texto_nombre_primer_actor.text().strip().lower()
        actor_dos_buscado = self.__vista._MainWindow__ui.texto_nombre_segundo_actor.text().strip().lower()

        if not actor_uno_buscado or not actor_dos_buscado:
            self.__vista.mostrar_alerta("Debe ingresar los nombres de dos actores")
            return

        resultados = []
        for pelicula in self.pelicula:
            actor_uno_coincide = any(actor_uno_buscado in actor.strip().lower() for actor in pelicula['actores'])
            actor_dos_coincide = any(actor_dos_buscado in actor.strip().lower() for actor in pelicula['actores'])

            if actor_uno_coincide and actor_dos_coincide:
                resultados.append(pelicula)

        if resultados:
            resultados.sort(key=lambda pelicula: pelicula['titulo'])
            self.mostrar_resultados(resultados)
        else:
            self.__vista.mostrar_alerta("Película no encontrada")

    def mostrar_resultados(self, resultados):
        self.__peliculas_mostradas = resultados[:10]

        for i, (label, boton) in enumerate(self.__frames):
            label_widget = getattr(self.__vista._MainWindow__ui, label)
            boton_widget = getattr(self.__vista._MainWindow__ui, boton)

            if i < len(self.__peliculas_mostradas):
                pelicula = self.__peliculas_mostradas[i]
                self.__vista.set_pelicula_info(label_widget, pelicula)
                label_widget.setVisible(True)
                boton_widget.setVisible(True)
                boton_widget.setText(pelicula['titulo'])
                try:
                    boton_widget.clicked.disconnect()
                except TypeError:
                    pass
                boton_widget.clicked.connect(lambda _, idx=i: self.abrir_segunda_ventana(idx))
            else:
                label_widget.setVisible(False)
                boton_widget.setVisible(False)
