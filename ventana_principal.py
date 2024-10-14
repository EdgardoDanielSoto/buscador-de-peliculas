# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_ventana_principal(object):
    def setupUi(self, ventana_principal):
        if not ventana_principal.objectName():
            ventana_principal.setObjectName(u"ventana_principal")
        ventana_principal.resize(821, 852)
        ventana_principal.setStyleSheet(u"background-color: rgb(236, 224, 208);")
        self.verticalLayout_3 = QVBoxLayout(ventana_principal)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.busquedas = QFrame(ventana_principal)
        self.busquedas.setObjectName(u"busquedas")
        self.busquedas.setFrameShape(QFrame.Shape.StyledPanel)
        self.busquedas.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.busquedas)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titulo_busqueda_pelicula = QLabel(self.busquedas)
        self.titulo_busqueda_pelicula.setObjectName(u"titulo_busqueda_pelicula")

        self.verticalLayout.addWidget(self.titulo_busqueda_pelicula)

        self.busqueda_pelicula = QFrame(self.busquedas)
        self.busqueda_pelicula.setObjectName(u"busqueda_pelicula")
        self.busqueda_pelicula.setStyleSheet(u"background-color: rgb(153, 193, 241);")
        self.busqueda_pelicula.setFrameShape(QFrame.Shape.Box)
        self.busqueda_pelicula.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout = QHBoxLayout(self.busqueda_pelicula)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.texto_busqueda_pelicula = QLineEdit(self.busqueda_pelicula)
        self.texto_busqueda_pelicula.setObjectName(u"texto_busqueda_pelicula")
        self.texto_busqueda_pelicula.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.texto_busqueda_pelicula)

        self.boton_buscar_pelicula = QPushButton(self.busqueda_pelicula)
        self.boton_buscar_pelicula.setObjectName(u"boton_buscar_pelicula")
        self.boton_buscar_pelicula.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.boton_buscar_pelicula)


        self.verticalLayout.addWidget(self.busqueda_pelicula)

        self.titulo_busqueda_actores = QLabel(self.busquedas)
        self.titulo_busqueda_actores.setObjectName(u"titulo_busqueda_actores")

        self.verticalLayout.addWidget(self.titulo_busqueda_actores)

        self.busqueda_actores = QFrame(self.busquedas)
        self.busqueda_actores.setObjectName(u"busqueda_actores")
        self.busqueda_actores.setStyleSheet(u"background-color: rgb(153, 193, 241);")
        self.busqueda_actores.setFrameShape(QFrame.Shape.Box)
        self.busqueda_actores.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.busqueda_actores)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.texto_nombre_primer_actor = QLineEdit(self.busqueda_actores)
        self.texto_nombre_primer_actor.setObjectName(u"texto_nombre_primer_actor")
        self.texto_nombre_primer_actor.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.texto_nombre_primer_actor)

        self.texto_nombre_segundo_actor = QLineEdit(self.busqueda_actores)
        self.texto_nombre_segundo_actor.setObjectName(u"texto_nombre_segundo_actor")
        self.texto_nombre_segundo_actor.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.texto_nombre_segundo_actor)

        self.boton_buscar_actores = QPushButton(self.busqueda_actores)
        self.boton_buscar_actores.setObjectName(u"boton_buscar_actores")
        self.boton_buscar_actores.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.boton_buscar_actores)


        self.verticalLayout.addWidget(self.busqueda_actores)


        self.verticalLayout_3.addWidget(self.busquedas)

        self.catalogo_peliculas = QFrame(ventana_principal)
        self.catalogo_peliculas.setObjectName(u"catalogo_peliculas")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catalogo_peliculas.sizePolicy().hasHeightForWidth())
        self.catalogo_peliculas.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.catalogo_peliculas)
        self.gridLayout.setObjectName(u"gridLayout")
        self.posicion_pelicula_siete = QFrame(self.catalogo_peliculas)
        self.posicion_pelicula_siete.setObjectName(u"posicion_pelicula_siete")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.posicion_pelicula_siete.sizePolicy().hasHeightForWidth())
        self.posicion_pelicula_siete.setSizePolicy(sizePolicy1)
        self.posicion_pelicula_siete.setFrameShape(QFrame.Shape.NoFrame)
        self.posicion_pelicula_siete.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.posicion_pelicula_siete)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.septima_pelicula_catalogo = QFrame(self.posicion_pelicula_siete)
        self.septima_pelicula_catalogo.setObjectName(u"septima_pelicula_catalogo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.septima_pelicula_catalogo.sizePolicy().hasHeightForWidth())
        self.septima_pelicula_catalogo.setSizePolicy(sizePolicy2)
        self.septima_pelicula_catalogo.setFrameShape(QFrame.Shape.NoFrame)
        self.septima_pelicula_catalogo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.septima_pelicula_catalogo)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.imagen_pelicula_siete = QLabel(self.septima_pelicula_catalogo)
        self.imagen_pelicula_siete.setObjectName(u"imagen_pelicula_siete")
        sizePolicy2.setHeightForWidth(self.imagen_pelicula_siete.sizePolicy().hasHeightForWidth())
        self.imagen_pelicula_siete.setSizePolicy(sizePolicy2)

        self.verticalLayout_18.addWidget(self.imagen_pelicula_siete)

        self.boton_nombre_pelicula_siete = QPushButton(self.septima_pelicula_catalogo)
        self.boton_nombre_pelicula_siete.setObjectName(u"boton_nombre_pelicula_siete")

        self.verticalLayout_18.addWidget(self.boton_nombre_pelicula_siete)


        self.verticalLayout_19.addWidget(self.septima_pelicula_catalogo)


        self.gridLayout.addWidget(self.posicion_pelicula_siete, 3, 0, 1, 1)

        self.posicion_pelicula_dos = QFrame(self.catalogo_peliculas)
        self.posicion_pelicula_dos.setObjectName(u"posicion_pelicula_dos")
        self.posicion_pelicula_dos.setFrameShape(QFrame.Shape.NoFrame)
        self.posicion_pelicula_dos.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.posicion_pelicula_dos)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.segunda_pelicula_catalogo = QFrame(self.posicion_pelicula_dos)
        self.segunda_pelicula_catalogo.setObjectName(u"segunda_pelicula_catalogo")
        sizePolicy1.setHeightForWidth(self.segunda_pelicula_catalogo.sizePolicy().hasHeightForWidth())
        self.segunda_pelicula_catalogo.setSizePolicy(sizePolicy1)
        self.segunda_pelicula_catalogo.setFrameShape(QFrame.Shape.NoFrame)
        self.segunda_pelicula_catalogo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.segunda_pelicula_catalogo)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.imagen_pelicula_dos = QLabel(self.segunda_pelicula_catalogo)
        self.imagen_pelicula_dos.setObjectName(u"imagen_pelicula_dos")
        sizePolicy2.setHeightForWidth(self.imagen_pelicula_dos.sizePolicy().hasHeightForWidth())
        self.imagen_pelicula_dos.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.imagen_pelicula_dos)

        self.boton_nombre_pelicula_dos = QPushButton(self.segunda_pelicula_catalogo)
        self.boton_nombre_pelicula_dos.setObjectName(u"boton_nombre_pelicula_dos")

        self.verticalLayout_5.addWidget(self.boton_nombre_pelicula_dos)


        self.verticalLayout_6.addWidget(self.segunda_pelicula_catalogo)


        self.gridLayout.addWidget(self.posicion_pelicula_dos, 0, 1, 1, 1)

        self.posicion_pelicula_uno = QFrame(self.catalogo_peliculas)
        self.posicion_pelicula_uno.setObjectName(u"posicion_pelicula_uno")
        self.posicion_pelicula_uno.setFrameShape(QFrame.Shape.NoFrame)
        self.posicion_pelicula_uno.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.posicion_pelicula_uno)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.primer_pelicula_catalogo = QFrame(self.posicion_pelicula_uno)
        self.primer_pelicula_catalogo.setObjectName(u"primer_pelicula_catalogo")
        sizePolicy1.setHeightForWidth(self.primer_pelicula_catalogo.sizePolicy().hasHeightForWidth())
        self.primer_pelicula_catalogo.setSizePolicy(sizePolicy1)
        self.primer_pelicula_catalogo.setFrameShape(QFrame.Shape.NoFrame)
        self.primer_pelicula_catalogo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.primer_pelicula_catalogo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.imagen_pelicula_uno = QLabel(self.primer_pelicula_catalogo)
        self.imagen_pelicula_uno.setObjectName(u"imagen_pelicula_uno")
        sizePolicy2.setHeightForWidth(self.imagen_pelicula_uno.sizePolicy().hasHeightForWidth())
        self.imagen_pelicula_uno.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.imagen_pelicula_uno)

        self.boton_nombre_pelicula_uno = QPushButton(self.primer_pelicula_catalogo)
        self.boton_nombre_pelicula_uno.setObjectName(u"boton_nombre_pelicula_uno")

        self.verticalLayout_2.addWidget(self.boton_nombre_pelicula_uno)


        self.verticalLayout_4.addWidget(self.primer_pelicula_catalogo)


        self.gridLayout.addWidget(self.posicion_pelicula_uno, 0, 0, 1, 1)

        self.posicion_pelicula_seis = QFrame(self.catalogo_peliculas)
        self.posicion_pelicula_seis.setObjectName(u"posicion_pelicula_seis")
        sizePolicy1.setHeightForWidth(self.posicion_pelicula_seis.sizePolicy().hasHeightForWidth())
        self.posicion_pelicula_seis.setSizePolicy(sizePolicy1)
        self.posicion_pelicula_seis.setFrameShape(QFrame.Shape.NoFrame)
        self.posicion_pelicula_seis.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.posicion_pelicula_seis)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.sexta_pelicula_catalogo = QFrame(self.posicion_pelicula_seis)
        self.sexta_pelicula_catalogo.setObjectName(u"sexta_pelicula_catalogo")
        sizePolicy2.setHeightForWidth(self.sexta_pelicula_catalogo.sizePolicy().hasHeightForWidth())
        self.sexta_pelicula_catalogo.setSizePolicy(sizePolicy2)
        self.sexta_pelicula_catalogo.setFrameShape(QFrame.Shape.NoFrame)
        self.sexta_pelicula_catalogo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.sexta_pelicula_catalogo)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.imagen_pelicula_seis = QLabel(self.sexta_pelicula_catalogo)
        self.imagen_pelicula_seis.setObjectName(u"imagen_pelicula_seis")
        sizePolicy2.setHeightForWidth(self.imagen_pelicula_seis.sizePolicy().hasHeightForWidth())
        self.imagen_pelicula_seis.setSizePolicy(sizePolicy2)

        self.verticalLayout_14.addWidget(self.imagen_pelicula_seis)

        self.boton_nombre_pelicula_seis = QPushButton(self.sexta_pelicula_catalogo)
        self.boton_nombre_pelicula_seis.setObjectName(u"boton_nombre_pelicula_seis")

        self.verticalLayout_14.addWidget(self.boton_nombre_pelicula_seis)


        self.verticalLayout_15.addWidget(self.sexta_pelicula_catalogo)


        self.gridLayout.addWidget(self.posicion_pelicula_seis, 2, 1, 1, 1)

        self.posicion_pelicula_diez = QFrame(self.catalogo_peliculas)
        self.posicion_pelicula_diez.setObjectName(u"posicion_pelicula_diez")
        sizePolicy1.setHeightForWidth(self.posicion_pelicula_diez.sizePolicy().hasHeightForWidth())
        self.posicion_pelicula_diez.setSizePolicy(sizePolicy1)
        self.posicion_pelicula_diez.setFrameShape(QFrame.Shape.NoFrame)
        self.posicion_pelicula_diez.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.posicion_pelicula_diez)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.decima_pelicula_catalogo = QFrame(self.posicion_pelicula_diez)
        self.decima_pelicula_catalogo.setObjectName(u"decima_pelicula_catalogo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.decima_pelicula_catalogo.sizePolicy().hasHeightForWidth())
        self.decima_pelicula_catalogo.setSizePolicy(sizePolicy3)
        self.decima_pelicula_catalogo.setFrameShape(QFrame.Shape.NoFrame)
        self.decima_pelicula_catalogo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.decima_pelicula_catalogo)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.imagen_pelicula_diez = QLabel(self.decima_pelicula_catalogo)
        self.imagen_pelicula_diez.setObjectName(u"imagen_pelicula_diez")
        sizePolicy2.setHeightForWidth(self.imagen_pelicula_diez.sizePolicy().hasHeightForWidth())
        self.imagen_pelicula_diez.setSizePolicy(sizePolicy2)

        self.verticalLayout_24.addWidget(self.imagen_pelicula_diez)

        self.boton_nombre_pelicula_diez = QPushButton(self.decima_pelicula_catalogo)
        self.boton_nombre_pelicula_diez.setObjectName(u"boton_nombre_pelicula_diez")

        self.verticalLayout_24.addWidget(self.boton_nombre_pelicula_diez)


        self.verticalLayout_25.addWidget(self.decima_pelicula_catalogo)


        self.gridLayout.addWidget(self.posicion_pelicula_diez, 4, 1, 1, 1)

        self.posicion_pelicula_cinco = QFrame(self.catalogo_peliculas)
        self.posicion_pelicula_cinco.setObjectName(u"posicion_pelicula_cinco")
        sizePolicy1.setHeightForWidth(self.posicion_pelicula_cinco.sizePolicy().hasHeightForWidth())
        self.posicion_pelicula_cinco.setSizePolicy(sizePolicy1)
        self.posicion_pelicula_cinco.setFrameShape(QFrame.Shape.NoFrame)
        self.posicion_pelicula_cinco.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.posicion_pelicula_cinco)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.quinta_pelicula_catalogo = QFrame(self.posicion_pelicula_cinco)
        self.quinta_pelicula_catalogo.setObjectName(u"quinta_pelicula_catalogo")
        sizePolicy2.setHeightForWidth(self.quinta_pelicula_catalogo.sizePolicy().hasHeightForWidth())
        self.quinta_pelicula_catalogo.setSizePolicy(sizePolicy2)
        self.quinta_pelicula_catalogo.setFrameShape(QFrame.Shape.NoFrame)
        self.quinta_pelicula_catalogo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.quinta_pelicula_catalogo)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.imagen_pelicula_cinco = QLabel(self.quinta_pelicula_catalogo)
        self.imagen_pelicula_cinco.setObjectName(u"imagen_pelicula_cinco")
        sizePolicy2.setHeightForWidth(self.imagen_pelicula_cinco.sizePolicy().hasHeightForWidth())
        self.imagen_pelicula_cinco.setSizePolicy(sizePolicy2)

        self.verticalLayout_20.addWidget(self.imagen_pelicula_cinco)

        self.boton_nombre_pelicula_cinco = QPushButton(self.quinta_pelicula_catalogo)
        self.boton_nombre_pelicula_cinco.setObjectName(u"boton_nombre_pelicula_cinco")

        self.verticalLayout_20.addWidget(self.boton_nombre_pelicula_cinco)


        self.verticalLayout_10.addWidget(self.quinta_pelicula_catalogo)


        self.gridLayout.addWidget(self.posicion_pelicula_cinco, 2, 0, 1, 1)

        self.posicion_pelicula_nueve = QFrame(self.catalogo_peliculas)
        self.posicion_pelicula_nueve.setObjectName(u"posicion_pelicula_nueve")
        sizePolicy1.setHeightForWidth(self.posicion_pelicula_nueve.sizePolicy().hasHeightForWidth())
        self.posicion_pelicula_nueve.setSizePolicy(sizePolicy1)
        self.posicion_pelicula_nueve.setFrameShape(QFrame.Shape.NoFrame)
        self.posicion_pelicula_nueve.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.posicion_pelicula_nueve)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.novena_pelicula_catalogo = QFrame(self.posicion_pelicula_nueve)
        self.novena_pelicula_catalogo.setObjectName(u"novena_pelicula_catalogo")
        sizePolicy3.setHeightForWidth(self.novena_pelicula_catalogo.sizePolicy().hasHeightForWidth())
        self.novena_pelicula_catalogo.setSizePolicy(sizePolicy3)
        self.novena_pelicula_catalogo.setFrameShape(QFrame.Shape.NoFrame)
        self.novena_pelicula_catalogo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.novena_pelicula_catalogo)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.imagen_pelicula_nueve = QLabel(self.novena_pelicula_catalogo)
        self.imagen_pelicula_nueve.setObjectName(u"imagen_pelicula_nueve")
        sizePolicy2.setHeightForWidth(self.imagen_pelicula_nueve.sizePolicy().hasHeightForWidth())
        self.imagen_pelicula_nueve.setSizePolicy(sizePolicy2)

        self.verticalLayout_22.addWidget(self.imagen_pelicula_nueve)

        self.boton_nombre_pelicula_nueve = QPushButton(self.novena_pelicula_catalogo)
        self.boton_nombre_pelicula_nueve.setObjectName(u"boton_nombre_pelicula_nueve")

        self.verticalLayout_22.addWidget(self.boton_nombre_pelicula_nueve)


        self.verticalLayout_23.addWidget(self.novena_pelicula_catalogo)


        self.gridLayout.addWidget(self.posicion_pelicula_nueve, 4, 0, 1, 1)

        self.posicion_pelicula_tres = QFrame(self.catalogo_peliculas)
        self.posicion_pelicula_tres.setObjectName(u"posicion_pelicula_tres")
        sizePolicy1.setHeightForWidth(self.posicion_pelicula_tres.sizePolicy().hasHeightForWidth())
        self.posicion_pelicula_tres.setSizePolicy(sizePolicy1)
        self.posicion_pelicula_tres.setFrameShape(QFrame.Shape.NoFrame)
        self.posicion_pelicula_tres.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.posicion_pelicula_tres)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tercer_pelicula_catalogo = QFrame(self.posicion_pelicula_tres)
        self.tercer_pelicula_catalogo.setObjectName(u"tercer_pelicula_catalogo")
        sizePolicy2.setHeightForWidth(self.tercer_pelicula_catalogo.sizePolicy().hasHeightForWidth())
        self.tercer_pelicula_catalogo.setSizePolicy(sizePolicy2)
        self.tercer_pelicula_catalogo.setFrameShape(QFrame.Shape.NoFrame)
        self.tercer_pelicula_catalogo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.tercer_pelicula_catalogo)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.imagen_pelicula_tres = QLabel(self.tercer_pelicula_catalogo)
        self.imagen_pelicula_tres.setObjectName(u"imagen_pelicula_tres")
        sizePolicy2.setHeightForWidth(self.imagen_pelicula_tres.sizePolicy().hasHeightForWidth())
        self.imagen_pelicula_tres.setSizePolicy(sizePolicy2)

        self.verticalLayout_9.addWidget(self.imagen_pelicula_tres)

        self.boton_nombre_pelicula_tres = QPushButton(self.tercer_pelicula_catalogo)
        self.boton_nombre_pelicula_tres.setObjectName(u"boton_nombre_pelicula_tres")

        self.verticalLayout_9.addWidget(self.boton_nombre_pelicula_tres)


        self.verticalLayout_11.addWidget(self.tercer_pelicula_catalogo)


        self.gridLayout.addWidget(self.posicion_pelicula_tres, 1, 0, 1, 1)

        self.posicion_pelicula_ocho = QFrame(self.catalogo_peliculas)
        self.posicion_pelicula_ocho.setObjectName(u"posicion_pelicula_ocho")
        sizePolicy1.setHeightForWidth(self.posicion_pelicula_ocho.sizePolicy().hasHeightForWidth())
        self.posicion_pelicula_ocho.setSizePolicy(sizePolicy1)
        self.posicion_pelicula_ocho.setFrameShape(QFrame.Shape.NoFrame)
        self.posicion_pelicula_ocho.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.posicion_pelicula_ocho)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.octava_pelicula_catalogo = QFrame(self.posicion_pelicula_ocho)
        self.octava_pelicula_catalogo.setObjectName(u"octava_pelicula_catalogo")
        sizePolicy2.setHeightForWidth(self.octava_pelicula_catalogo.sizePolicy().hasHeightForWidth())
        self.octava_pelicula_catalogo.setSizePolicy(sizePolicy2)
        self.octava_pelicula_catalogo.setFrameShape(QFrame.Shape.NoFrame)
        self.octava_pelicula_catalogo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.octava_pelicula_catalogo)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.imagen_pelicula_ocho = QLabel(self.octava_pelicula_catalogo)
        self.imagen_pelicula_ocho.setObjectName(u"imagen_pelicula_ocho")
        sizePolicy2.setHeightForWidth(self.imagen_pelicula_ocho.sizePolicy().hasHeightForWidth())
        self.imagen_pelicula_ocho.setSizePolicy(sizePolicy2)

        self.verticalLayout_21.addWidget(self.imagen_pelicula_ocho)

        self.boton_nombre_pelicula_ocho = QPushButton(self.octava_pelicula_catalogo)
        self.boton_nombre_pelicula_ocho.setObjectName(u"boton_nombre_pelicula_ocho")

        self.verticalLayout_21.addWidget(self.boton_nombre_pelicula_ocho)


        self.verticalLayout_8.addWidget(self.octava_pelicula_catalogo)


        self.gridLayout.addWidget(self.posicion_pelicula_ocho, 3, 1, 1, 1)

        self.posicion_pelicula_cuatro = QFrame(self.catalogo_peliculas)
        self.posicion_pelicula_cuatro.setObjectName(u"posicion_pelicula_cuatro")
        sizePolicy1.setHeightForWidth(self.posicion_pelicula_cuatro.sizePolicy().hasHeightForWidth())
        self.posicion_pelicula_cuatro.setSizePolicy(sizePolicy1)
        self.posicion_pelicula_cuatro.setFrameShape(QFrame.Shape.NoFrame)
        self.posicion_pelicula_cuatro.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.posicion_pelicula_cuatro)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.cuarta_pelicula_catalogo = QFrame(self.posicion_pelicula_cuatro)
        self.cuarta_pelicula_catalogo.setObjectName(u"cuarta_pelicula_catalogo")
        sizePolicy2.setHeightForWidth(self.cuarta_pelicula_catalogo.sizePolicy().hasHeightForWidth())
        self.cuarta_pelicula_catalogo.setSizePolicy(sizePolicy2)
        self.cuarta_pelicula_catalogo.setFrameShape(QFrame.Shape.NoFrame)
        self.cuarta_pelicula_catalogo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.cuarta_pelicula_catalogo)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.imagen_pelicula_cuatro = QLabel(self.cuarta_pelicula_catalogo)
        self.imagen_pelicula_cuatro.setObjectName(u"imagen_pelicula_cuatro")
        sizePolicy2.setHeightForWidth(self.imagen_pelicula_cuatro.sizePolicy().hasHeightForWidth())
        self.imagen_pelicula_cuatro.setSizePolicy(sizePolicy2)

        self.verticalLayout_12.addWidget(self.imagen_pelicula_cuatro)

        self.boton_nombre_pelicula_cuatro = QPushButton(self.cuarta_pelicula_catalogo)
        self.boton_nombre_pelicula_cuatro.setObjectName(u"boton_nombre_pelicula_cuatro")

        self.verticalLayout_12.addWidget(self.boton_nombre_pelicula_cuatro)


        self.verticalLayout_13.addWidget(self.cuarta_pelicula_catalogo)


        self.gridLayout.addWidget(self.posicion_pelicula_cuatro, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.catalogo_peliculas)


        self.retranslateUi(ventana_principal)

        QMetaObject.connectSlotsByName(ventana_principal)
    # setupUi

    def retranslateUi(self, ventana_principal):
        ventana_principal.setWindowTitle(QCoreApplication.translate("ventana_principal", u"Peliculas argentinas", None))
        self.titulo_busqueda_pelicula.setText(QCoreApplication.translate("ventana_principal", u"Buscar pelicula", None))
        self.texto_busqueda_pelicula.setPlaceholderText(QCoreApplication.translate("ventana_principal", u"ingrese aqu\u00ed nombre de pelicula", None))
        self.boton_buscar_pelicula.setText(QCoreApplication.translate("ventana_principal", u"Buscar", None))
        self.titulo_busqueda_actores.setText(QCoreApplication.translate("ventana_principal", u"Buscar por actores", None))
        self.texto_nombre_primer_actor.setPlaceholderText(QCoreApplication.translate("ventana_principal", u"Ingrese nombre primer actor ", None))
        self.texto_nombre_segundo_actor.setPlaceholderText(QCoreApplication.translate("ventana_principal", u"Ingrese nombre segundo actor", None))
        self.boton_buscar_actores.setText(QCoreApplication.translate("ventana_principal", u"Buscar", None))
        self.imagen_pelicula_siete.setText("")
        self.boton_nombre_pelicula_siete.setText(QCoreApplication.translate("ventana_principal", u"info", None))
        self.imagen_pelicula_dos.setText("")
        self.boton_nombre_pelicula_dos.setText(QCoreApplication.translate("ventana_principal", u"info", None))
        self.imagen_pelicula_uno.setText("")
        self.boton_nombre_pelicula_uno.setText(QCoreApplication.translate("ventana_principal", u"info", None))
        self.imagen_pelicula_seis.setText("")
        self.boton_nombre_pelicula_seis.setText(QCoreApplication.translate("ventana_principal", u"info", None))
        self.imagen_pelicula_diez.setText("")
        self.boton_nombre_pelicula_diez.setText(QCoreApplication.translate("ventana_principal", u"info", None))
        self.imagen_pelicula_cinco.setText("")
        self.boton_nombre_pelicula_cinco.setText(QCoreApplication.translate("ventana_principal", u"info", None))
        self.imagen_pelicula_nueve.setText("")
        self.boton_nombre_pelicula_nueve.setText(QCoreApplication.translate("ventana_principal", u"info", None))
        self.imagen_pelicula_tres.setText("")
        self.boton_nombre_pelicula_tres.setText(QCoreApplication.translate("ventana_principal", u"info", None))
        self.imagen_pelicula_ocho.setText("")
        self.boton_nombre_pelicula_ocho.setText(QCoreApplication.translate("ventana_principal", u"info", None))
        self.imagen_pelicula_cuatro.setText("")
        self.boton_nombre_pelicula_cuatro.setText(QCoreApplication.translate("ventana_principal", u"info", None))
    # retranslateUi

