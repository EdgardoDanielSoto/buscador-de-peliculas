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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ventana_principal(object):
    def setupUi(self, ventana_principal):
        if not ventana_principal.objectName():
            ventana_principal.setObjectName(u"ventana_principal")
        ventana_principal.resize(592, 669)
        ventana_principal.setStyleSheet(u"background-color: rgb(246, 245, 244);")
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
        self.busqueda_pelicula.setStyleSheet(u"background-color: rgb(192, 191, 188);")
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
        self.busqueda_actores.setStyleSheet(u"\n"
"background-color: rgb(192, 191, 188);")
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

        self.table_peliculas = QTableWidget(self.busquedas)
        self.table_peliculas.setObjectName(u"table_peliculas")

        self.verticalLayout.addWidget(self.table_peliculas)


        self.verticalLayout_3.addWidget(self.busquedas)


        self.retranslateUi(ventana_principal)

        QMetaObject.connectSlotsByName(ventana_principal)
    # setupUi

    def retranslateUi(self, ventana_principal):
        ventana_principal.setWindowTitle(QCoreApplication.translate("ventana_principal", u"Peliculas argentinas", None))
        self.titulo_busqueda_pelicula.setText(QCoreApplication.translate("ventana_principal", u"Buscar pelicula", None))
        self.texto_busqueda_pelicula.setPlaceholderText(QCoreApplication.translate("ventana_principal", u"nombre de pelicula", None))
        self.boton_buscar_pelicula.setText(QCoreApplication.translate("ventana_principal", u"Buscar - Recargar", None))
        self.titulo_busqueda_actores.setText(QCoreApplication.translate("ventana_principal", u"Buscar por actores", None))
        self.texto_nombre_primer_actor.setPlaceholderText(QCoreApplication.translate("ventana_principal", u"nombre primer actor", None))
        self.texto_nombre_segundo_actor.setPlaceholderText(QCoreApplication.translate("ventana_principal", u"nombre segundo actor", None))
        self.boton_buscar_actores.setText(QCoreApplication.translate("ventana_principal", u"Buscar", None))
    # retranslateUi

