from vista.ventana_de_busqueda import VentanaPrincipal
from vista.descripcion_pelicula import VentanaPelicula
from modelos.actor import Actor
from modelos.pelicula import Pelicula
from modelos.catalogo import Catalogo


class Controlador:
    def __init__(self):
        self.__catalogo = Catalogo()
        self.__cargar_datos()
        self.__peliculas = self.__catalogo.obtener_peliculas()


        self.__ventana_principal = VentanaPrincipal(self.__catalogo)
        self.__ventana_principal.cargar_peliculas(self.__peliculas)
        self.__ventana_principal.buscar.connect(self.__buscar_peliculas)
        self.__ventana_principal.abrir_pelicula.connect(self.__mostrar_pelicula)
        self.__ventana_principal.buscar_pelicula_actores.connect(self.__buscar_por_actores)

        self.__ventana_pelicula = VentanaPelicula()

    def __cargar_datos(self):
        contenido = self.__catalogo.obtener_contenido_del_archivo()
        for pelicula in contenido:
            actores = []
            for nombre in pelicula["actores"]:
                actores.append(Actor(nombre))

            nueva_pelicula = Pelicula(
                pelicula["titulo"],
                pelicula["sinopsis"],
                pelicula["Puntuacion"],
                actores,
                pelicula["poster"]
            )
            self.__catalogo.agregar_pelicula(nueva_pelicula)

    def __buscar_peliculas(self, titulo):
        peliculas = self.__catalogo.buscar_peliculas_por_titulo(titulo)
        if len(peliculas) == 0:
            self.__ventana_principal.mostrar_error("No se encontró la película")
            peliculas = self.__catalogo.obtener_peliculas()

        self.__ventana_principal.cargar_peliculas(peliculas)

    def __mostrar_pelicula(self, titulo):
        peliculas = self.__catalogo.buscar_peliculas_por_titulo(titulo)

        if peliculas:
            pelicula = peliculas[0]
            self.__ventana_pelicula.mostrar_datos(pelicula)

            self.__ventana_pelicula.exec()
        else:
            self.__ventana_principal.mostrar_error("No se encontró la película.")


    def __buscar_por_actores(self, actor_n1, actor_n2):
        if actor_n1 and actor_n2:
            if actor_n1 != actor_n2:
                peliculas_encontradas = self.__catalogo.buscar_peliculas_por_actores(actor_n1, actor_n2)

                if len(peliculas_encontradas) == 0:
                    self.__ventana_principal.mostrar_error("No se encontraron películas con esos actores.")
                else:
                    self.__ventana_principal.cargar_peliculas(peliculas_encontradas)
            else:
                self.__ventana_principal.mostrar_error("Los actores no pueden ser los mismos.")
        else:
            self.__ventana_principal.mostrar_error("Ingrese ambos nombres de actores.")

    def ejecutar(self):
        self.__ventana_principal.show()

