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
    QVBoxLayout, QWidget)

class Ui_SegundaVentana(object):
    def setupUi(self, SegundaVentana):
        if not SegundaVentana.objectName():
            SegundaVentana.setObjectName(u"SegundaVentana")
        SegundaVentana.resize(608, 335)
        SegundaVentana.setMinimumSize(QSize(608, 335))
        SegundaVentana.setMaximumSize(QSize(608, 335))
        self.verticalLayout = QVBoxLayout(SegundaVentana)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.descripcion_imagen_texto = QFrame(SegundaVentana)
        self.descripcion_imagen_texto.setObjectName(u"descripcion_imagen_texto")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.descripcion_imagen_texto.sizePolicy().hasHeightForWidth())
        self.descripcion_imagen_texto.setSizePolicy(sizePolicy)
        self.descripcion_imagen_texto.setFrameShape(QFrame.Shape.Box)
        self.descripcion_imagen_texto.setFrameShadow(QFrame.Shadow.Plain)
        self.descripcion_imagen = QFrame(self.descripcion_imagen_texto)
        self.descripcion_imagen.setObjectName(u"descripcion_imagen")
        self.descripcion_imagen.setGeometry(QRect(10, 10, 200, 300))
        sizePolicy.setHeightForWidth(self.descripcion_imagen.sizePolicy().hasHeightForWidth())
        self.descripcion_imagen.setSizePolicy(sizePolicy)
        self.descripcion_imagen.setFrameShape(QFrame.Shape.StyledPanel)
        self.descripcion_imagen.setFrameShadow(QFrame.Shadow.Plain)
        self.imagen_descripcion = QLabel(self.descripcion_imagen)
        self.imagen_descripcion.setObjectName(u"imagen_descripcion")
        self.imagen_descripcion.setGeometry(QRect(10, 10, 180, 280))
        sizePolicy.setHeightForWidth(self.imagen_descripcion.sizePolicy().hasHeightForWidth())
        self.imagen_descripcion.setSizePolicy(sizePolicy)
        self.descripcion_texto = QFrame(self.descripcion_imagen_texto)
        self.descripcion_texto.setObjectName(u"descripcion_texto")
        self.descripcion_texto.setGeometry(QRect(220, 10, 360, 300))
        self.descripcion_texto.setFrameShape(QFrame.Shape.StyledPanel)
        self.descripcion_texto.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.descripcion_texto)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.encabezado_sinopsis = QLabel(self.descripcion_texto)
        self.encabezado_sinopsis.setObjectName(u"encabezado_sinopsis")

        self.verticalLayout_3.addWidget(self.encabezado_sinopsis)

        self.texto_sinopsis = QLabel(self.descripcion_texto)
        self.texto_sinopsis.setObjectName(u"texto_sinopsis")
        sizePolicy.setHeightForWidth(self.texto_sinopsis.sizePolicy().hasHeightForWidth())
        self.texto_sinopsis.setSizePolicy(sizePolicy)
        self.texto_sinopsis.setStyleSheet(u"")
        self.texto_sinopsis.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout_3.addWidget(self.texto_sinopsis)

        self.encabezado_elenco = QLabel(self.descripcion_texto)
        self.encabezado_elenco.setObjectName(u"encabezado_elenco")

        self.verticalLayout_3.addWidget(self.encabezado_elenco)

        self.nombres_actores = QLabel(self.descripcion_texto)
        self.nombres_actores.setObjectName(u"nombres_actores")
        self.nombres_actores.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout_3.addWidget(self.nombres_actores)


        self.verticalLayout.addWidget(self.descripcion_imagen_texto)


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
    # retranslateUi

