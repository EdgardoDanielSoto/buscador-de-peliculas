# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'segunda_ventana.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QWidget)

class Ui_SegundaVentana(object):
    def setupUi(self, SegundaVentana):
        if not SegundaVentana.objectName():
            SegundaVentana.setObjectName(u"SegundaVentana")
        SegundaVentana.setEnabled(True)
        SegundaVentana.resize(903, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(SegundaVentana.sizePolicy().hasHeightForWidth())
        SegundaVentana.setSizePolicy(sizePolicy)
        SegundaVentana.setMinimumSize(QSize(903, 400))
        SegundaVentana.setMaximumSize(QSize(903, 400))
        SegundaVentana.setSizeIncrement(QSize(0, 0))
        self.descripcion_imagen_texto = QFrame(SegundaVentana)
        self.descripcion_imagen_texto.setObjectName(u"descripcion_imagen_texto")
        self.descripcion_imagen_texto.setGeometry(QRect(9, 9, 881, 381))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.descripcion_imagen_texto.sizePolicy().hasHeightForWidth())
        self.descripcion_imagen_texto.setSizePolicy(sizePolicy1)
        self.descripcion_imagen_texto.setFrameShape(QFrame.Shape.Box)
        self.descripcion_imagen_texto.setFrameShadow(QFrame.Shadow.Plain)
        self.descripcion_imagen = QFrame(self.descripcion_imagen_texto)
        self.descripcion_imagen.setObjectName(u"descripcion_imagen")
        self.descripcion_imagen.setGeometry(QRect(10, 10, 201, 341))
        sizePolicy1.setHeightForWidth(self.descripcion_imagen.sizePolicy().hasHeightForWidth())
        self.descripcion_imagen.setSizePolicy(sizePolicy1)
        self.descripcion_imagen.setFrameShape(QFrame.Shape.StyledPanel)
        self.descripcion_imagen.setFrameShadow(QFrame.Shadow.Plain)
        self.imagen_descripcion = QLabel(self.descripcion_imagen)
        self.imagen_descripcion.setObjectName(u"imagen_descripcion")
        self.imagen_descripcion.setGeometry(QRect(10, 10, 181, 321))
        sizePolicy1.setHeightForWidth(self.imagen_descripcion.sizePolicy().hasHeightForWidth())
        self.imagen_descripcion.setSizePolicy(sizePolicy1)
        self.descripcion_texto = QFrame(self.descripcion_imagen_texto)
        self.descripcion_texto.setObjectName(u"descripcion_texto")
        self.descripcion_texto.setGeometry(QRect(210, 10, 661, 341))
        self.descripcion_texto.setFrameShape(QFrame.Shape.StyledPanel)
        self.descripcion_texto.setFrameShadow(QFrame.Shadow.Plain)
        self.encabezado_sinopsis = QLabel(self.descripcion_texto)
        self.encabezado_sinopsis.setObjectName(u"encabezado_sinopsis")
        self.encabezado_sinopsis.setGeometry(QRect(10, 40, 67, 20))
        self.texto_sinopsis = QLabel(self.descripcion_texto)
        self.texto_sinopsis.setObjectName(u"texto_sinopsis")
        self.texto_sinopsis.setGeometry(QRect(10, 35, 641, 141))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.texto_sinopsis.sizePolicy().hasHeightForWidth())
        self.texto_sinopsis.setSizePolicy(sizePolicy2)
        self.encabezado_elenco = QLabel(self.descripcion_texto)
        self.encabezado_elenco.setObjectName(u"encabezado_elenco")
        self.encabezado_elenco.setGeometry(QRect(10, 220, 56, 20))
        self.nombres_actores = QLabel(self.descripcion_texto)
        self.nombres_actores.setObjectName(u"nombres_actores")
        self.nombres_actores.setGeometry(QRect(10, 220, 641, 61))
        sizePolicy2.setHeightForWidth(self.nombres_actores.sizePolicy().hasHeightForWidth())
        self.nombres_actores.setSizePolicy(sizePolicy2)
        self.nombres_actores.setFrameShape(QFrame.Shape.NoFrame)
        self.puntuacion = QLabel(self.descripcion_texto)
        self.puntuacion.setObjectName(u"puntuacion")
        self.puntuacion.setGeometry(QRect(120, 290, 81, 19))
        sizePolicy2.setHeightForWidth(self.puntuacion.sizePolicy().hasHeightForWidth())
        self.puntuacion.setSizePolicy(sizePolicy2)
        self.encabezado_puntuacion = QLabel(self.descripcion_texto)
        self.encabezado_puntuacion.setObjectName(u"encabezado_puntuacion")
        self.encabezado_puntuacion.setGeometry(QRect(10, 290, 100, 20))
        self.encabezado_puntuacion.setFrameShape(QFrame.Shape.NoFrame)
        self.encabezado_puntuacion.setFrameShadow(QFrame.Shadow.Plain)

        self.retranslateUi(SegundaVentana)

        QMetaObject.connectSlotsByName(SegundaVentana)
    # setupUi

    def retranslateUi(self, SegundaVentana):
        SegundaVentana.setWindowTitle(QCoreApplication.translate("SegundaVentana", u"Informaci\u00f3n de pelicula ", None))
        self.imagen_descripcion.setText("")
        self.encabezado_sinopsis.setText(QCoreApplication.translate("SegundaVentana", u"Sinopsis:", None))
        self.texto_sinopsis.setText("")
        self.encabezado_elenco.setText(QCoreApplication.translate("SegundaVentana", u"Elenco:", None))
        self.nombres_actores.setText("")
        self.puntuacion.setText("")
        self.encabezado_puntuacion.setText(QCoreApplication.translate("SegundaVentana", u"Puntuacion : ", None))
    # retranslateUi

