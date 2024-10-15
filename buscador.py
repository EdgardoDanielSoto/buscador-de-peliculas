import sys
import random
from PySide6.QtWidgets import QApplication, QCompleter
from PySide6.QtCore import Qt
from listado_peliculas import ListaPeliculas
from ventanas import MainWindow, SegundaVentana

class _BuscadorPeliculas:
    def __init__(self, modelo, vista):
        self.__model = modelo
        self.__view = vista
        self.__peliculas = self.__model.get_peliculas()

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

        frames = [
            ('primer_pelicula_catalogo', 'boton_nombre_pelicula_uno'),
            ('segunda_pelicula_catalogo', 'boton_nombre_pelicula_dos'),
            ('tercer_pelicula_catalogo', 'boton_nombre_pelicula_tres'),
            ('cuarta_pelicula_catalogo', 'boton_nombre_pelicula_cuatro'),
            ('quinta_pelicula_catalogo', 'boton_nombre_pelicula_cinco'),
            ('sexta_pelicula_catalogo', 'boton_nombre_pelicula_seis'),
            ('septima_pelicula_catalogo', 'boton_nombre_pelicula_siete'),
            ('octava_pelicula_catalogo', 'boton_nombre_pelicula_ocho'),
            ('novena_pelicula_catalogo', 'boton_nombre_pelicula_nueve'),
            ('decima_pelicula_catalogo', 'boton_nombre_pelicula_diez')
        ]

        for i, (frame, boton) in enumerate(frames):
            frame_widget = getattr(self.__view._MainWindow__ui, frame)
            boton_widget = getattr(self.__view._MainWindow__ui, boton)
            boton_widget.clicked.connect(lambda _, idx=i: self.abrir_segunda_ventana(idx))

        self.mostrar_todas_peliculas()

    def abrir_segunda_ventana(self, index):
        if index < len(self.__peliculas):
            pelicula = self.__peliculas[index]
            ventana_informacion = SegundaVentana(pelicula, self.__view)
            ventana_informacion.exec()

    def mostrar_todas_peliculas(self):
        labels = [
            self.__view._MainWindow__ui.imagen_pelicula_uno, self.__view._MainWindow__ui.imagen_pelicula_dos, self.__view._MainWindow__ui.imagen_pelicula_tres,
            self.__view._MainWindow__ui.imagen_pelicula_cuatro, self.__view._MainWindow__ui.imagen_pelicula_cinco, self.__view._MainWindow__ui.imagen_pelicula_seis,
            self.__view._MainWindow__ui.imagen_pelicula_siete, self.__view._MainWindow__ui.imagen_pelicula_ocho, self.__view._MainWindow__ui.imagen_pelicula_nueve,
            self.__view._MainWindow__ui.imagen_pelicula_diez
        ]
        botones = [
            self.__view._MainWindow__ui.boton_nombre_pelicula_uno, self.__view._MainWindow__ui.boton_nombre_pelicula_dos, self.__view._MainWindow__ui.boton_nombre_pelicula_tres,
            self.__view._MainWindow__ui.boton_nombre_pelicula_cuatro, self.__view._MainWindow__ui.boton_nombre_pelicula_cinco, self.__view._MainWindow__ui.boton_nombre_pelicula_seis,
            self.__view._MainWindow__ui.boton_nombre_pelicula_siete, self.__view._MainWindow__ui.boton_nombre_pelicula_ocho, self.__view._MainWindow__ui.boton_nombre_pelicula_nueve,
            self.__view._MainWindow__ui.boton_nombre_pelicula_diez
        ]

        random.shuffle(self.__peliculas)

        for label, boton, pelicula in zip(labels, botones, self.__peliculas):
            self.__view.set_pelicula_info(label, pelicula)
            label.setVisible(True)
            boton.setVisible(True)

    def __buscar_por_titulo(self):
        nombre_buscado = self.__view._MainWindow__ui.texto_busqueda_pelicula.text().strip().lower()

        if not nombre_buscado:
            self.mostrar_todas_peliculas()
            return

        resultados = [pelicula for pelicula in self.__peliculas if nombre_buscado in pelicula['titulo'].strip().lower()]

        if resultados:
            resultados.sort(key=lambda pelicula: pelicula['titulo'])
            self.mostrar_resultados(resultados)
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
            self.mostrar_resultados(resultados)
        else:
            self.__view.mostrar_alerta("Película no encontrada")

    def mostrar_resultados(self, resultados):
        labels = [
            self.__view._MainWindow__ui.imagen_pelicula_uno, self.__view._MainWindow__ui.imagen_pelicula_dos, self.__view._MainWindow__ui.imagen_pelicula_tres,
            self.__view._MainWindow__ui.imagen_pelicula_cuatro, self.__view._MainWindow__ui.imagen_pelicula_cinco, self.__view._MainWindow__ui.imagen_pelicula_seis,
            self.__view._MainWindow__ui.imagen_pelicula_siete, self.__view._MainWindow__ui.imagen_pelicula_ocho, self.__view._MainWindow__ui.imagen_pelicula_nueve,
            self.__view._MainWindow__ui.imagen_pelicula_diez
        ]
        botones = [
            self.__view._MainWindow__ui.boton_nombre_pelicula_uno, self.__view._MainWindow__ui.boton_nombre_pelicula_dos, self.__view._MainWindow__ui.boton_nombre_pelicula_tres,
            self.__view._MainWindow__ui.boton_nombre_pelicula_cuatro, self.__view._MainWindow__ui.boton_nombre_pelicula_cinco, self.__view._MainWindow__ui.boton_nombre_pelicula_seis,
            self.__view._MainWindow__ui.boton_nombre_pelicula_siete, self.__view._MainWindow__ui.boton_nombre_pelicula_ocho, self.__view._MainWindow__ui.boton_nombre_pelicula_nueve,
            self.__view._MainWindow__ui.boton_nombre_pelicula_diez
        ]

        for label, boton in zip(labels, botones):
            label.clear()
            label.setVisible(False)
            boton.setVisible(False)

        for indice, (label, boton, pelicula) in enumerate(zip(labels, botones, resultados)):
            self.__view.set_pelicula_info(label, pelicula)
            label.setVisible(True)
            boton.setVisible(True)
            boton.setText(pelicula['titulo'])
            boton.clicked.disconnect()
            boton.clicked.connect(lambda _, idx=indice: self.abrir_segunda_ventana(idx))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    modelo = ListaPeliculas('portadas/peliculas.json')
    vista = MainWindow()
    controlador = _BuscadorPeliculas(modelo, vista)
    vista.show()
    sys.exit(app.exec())