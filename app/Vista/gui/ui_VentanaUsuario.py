# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaUsuarioeHnCkl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import app.Vista.gui.imagenes_rc


class Ui_VentanaUsuario(object):
    def setupUi(self, VentanaUsuario):
        if not VentanaUsuario.objectName():
            VentanaUsuario.setObjectName(u"VentanaUsuario")
        VentanaUsuario.resize(333, 500)
        VentanaUsuario.setMinimumSize(QSize(333, 500))
        VentanaUsuario.setMaximumSize(QSize(333, 500))
        VentanaUsuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame = QFrame(VentanaUsuario)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 333, 61))
        self.frame.setMinimumSize(QSize(333, 51))
        self.frame.setStyleSheet(u"background-color:  rgb(255, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 10, 91, 41))
        self.label.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 20pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(182, 10, 141, 41))
        self.label_2.setStyleSheet(u"image: url(:/imagenes/imagenes/logo-udemedellin-footer.png);")
        self.label_2.setPixmap(QPixmap(u"../imagenes/logo-udemedellin-footer.png"))
        self.label_2.setScaledContents(True)
        self.pbutton_cerrar_sesion = QPushButton(self.frame)
        self.pbutton_cerrar_sesion.setObjectName(u"pbutton_cerrar_sesion")
        self.pbutton_cerrar_sesion.setGeometry(QRect(0, 10, 41, 41))
        self.pbutton_cerrar_sesion.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbutton_cerrar_sesion.setStyleSheet(u"background-color:rgba(0,0,0,0%);\n"
"image: url(:/imagenes/imagenes/cerrar-sesion.png);")
        icon = QIcon()
        icon.addFile(u"../imagenes/envelope.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbutton_cerrar_sesion.setIcon(icon)
        self.pbutton_cerrar_sesion.setIconSize(QSize(40, 30))
        self.frame_2 = QFrame(VentanaUsuario)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 61, 333, 439))
        self.frame_2.setMinimumSize(QSize(333, 439))
        self.frame_2.setMaximumSize(QSize(333, 439))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 390, 333, 3))
        self.line.setMinimumSize(QSize(333, 0))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.tbutton_noticias = QToolButton(self.frame_2)
        self.tbutton_noticias.setObjectName(u"tbutton_noticias")
        self.tbutton_noticias.setGeometry(QRect(100, 400, 48, 30))
        self.tbutton_noticias.setMinimumSize(QSize(48, 30))
        self.tbutton_noticias.setMaximumSize(QSize(48, 30))
        self.tbutton_noticias.setCursor(QCursor(Qt.PointingHandCursor))
        self.tbutton_noticias.setStyleSheet(u"background-color:rgba(0,0,0,0%);\n"
"image: url(:/imagenes/imagenes/forma.png);\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../imagenes/forma.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbutton_noticias.setIcon(icon1)
        self.tbutton_noticias.setIconSize(QSize(40, 30))
        self.tbutton_opinion = QToolButton(self.frame_2)
        self.tbutton_opinion.setObjectName(u"tbutton_opinion")
        self.tbutton_opinion.setGeometry(QRect(20, 400, 48, 30))
        self.tbutton_opinion.setMinimumSize(QSize(48, 30))
        self.tbutton_opinion.setMaximumSize(QSize(48, 30))
        self.tbutton_opinion.setCursor(QCursor(Qt.PointingHandCursor))
        self.tbutton_opinion.setStyleSheet(u"background-color:rgba(0,0,0,0%);\n"
"image: url(:/imagenes/imagenes/envelope.png);")
        self.tbutton_opinion.setIcon(icon)
        self.tbutton_opinion.setIconSize(QSize(40, 30))
        self.tbutton_usuario = QToolButton(self.frame_2)
        self.tbutton_usuario.setObjectName(u"tbutton_usuario")
        self.tbutton_usuario.setGeometry(QRect(260, 370, 48, 61))
        self.tbutton_usuario.setMinimumSize(QSize(48, 33))
        self.tbutton_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.tbutton_usuario.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius: 20px;\n"
"image: url(:/imagenes/imagenes/user (1).png);")
        icon2 = QIcon()
        icon2.addFile(u"../imagenes/user (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbutton_usuario.setIcon(icon2)
        self.tbutton_usuario.setIconSize(QSize(40, 30))
        self.tbutton_reserva = QToolButton(self.frame_2)
        self.tbutton_reserva.setObjectName(u"tbutton_reserva")
        self.tbutton_reserva.setGeometry(QRect(180, 400, 48, 30))
        self.tbutton_reserva.setMinimumSize(QSize(48, 30))
        self.tbutton_reserva.setMaximumSize(QSize(48, 30))
        self.tbutton_reserva.setCursor(QCursor(Qt.PointingHandCursor))
        self.tbutton_reserva.setStyleSheet(u"background-color:rgba(0,0,0,0%);\n"
"image: url(:/imagenes/imagenes/calendar-clock.png);")
        icon3 = QIcon()
        icon3.addFile(u"../imagenes/calendar-clock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbutton_reserva.setIcon(icon3)
        self.tbutton_reserva.setIconSize(QSize(40, 30))
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 50, 333, 281))
        self.frame_3.setMinimumSize(QSize(333, 241))
        self.frame_3.setLayoutDirection(Qt.LeftToRight)
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(25)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(9, -1, 9, 9)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(31, 32))
        self.label_4.setStyleSheet(u"image: url(:/imagenes/imagenes/circle-phone-flip.png);")
        self.label_4.setPixmap(QPixmap(u"../imagenes/circle-phone-flip.png"))
        self.label_4.setScaledContents(True)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_edad = QLabel(self.frame_3)
        self.label_edad.setObjectName(u"label_edad")
        self.label_edad.setMinimumSize(QSize(191, 36))
        self.label_edad.setMaximumSize(QSize(191, 36))
        self.label_edad.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")

        self.gridLayout.addWidget(self.label_edad, 5, 1, 1, 1)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(31, 32))
        self.label_6.setStyleSheet(u"image: url(:/imagenes/imagenes/sobre (2).png);")
        self.label_6.setPixmap(QPixmap(u"../imagenes/sobre (2).png"))
        self.label_6.setScaledContents(True)

        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)

        self.label_nombre = QLabel(self.frame_3)
        self.label_nombre.setObjectName(u"label_nombre")
        self.label_nombre.setMinimumSize(QSize(191, 36))
        self.label_nombre.setMaximumSize(QSize(191, 36))
        self.label_nombre.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")

        self.gridLayout.addWidget(self.label_nombre, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(31, 32))
        self.label_8.setStyleSheet(u"image: url(:/imagenes/imagenes/genero.png);")
        self.label_8.setPixmap(QPixmap(u"../imagenes/sobre (2).png"))
        self.label_8.setScaledContents(True)

        self.gridLayout.addWidget(self.label_8, 9, 0, 1, 1)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(31, 32))
        self.label_7.setStyleSheet(u"image: url(:/imagenes/imagenes/usuario.png);")
        self.label_7.setPixmap(QPixmap(u"../imagenes/usuario.png"))
        self.label_7.setScaledContents(True)

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.label_correo = QLabel(self.frame_3)
        self.label_correo.setObjectName(u"label_correo")
        self.label_correo.setMinimumSize(QSize(191, 36))
        self.label_correo.setMaximumSize(QSize(191, 36))
        self.label_correo.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")

        self.gridLayout.addWidget(self.label_correo, 7, 1, 1, 1)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(31, 32))
        self.label_5.setStyleSheet(u"image: url(:/imagenes/imagenes/age-group (1).png);")
        self.label_5.setPixmap(QPixmap(u"../imagenes/id-insignia.png"))
        self.label_5.setScaledContents(True)

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 6, 1, 1, 1)

        self.label_sexo = QLabel(self.frame_3)
        self.label_sexo.setObjectName(u"label_sexo")
        self.label_sexo.setMinimumSize(QSize(191, 36))
        self.label_sexo.setMaximumSize(QSize(191, 36))
        self.label_sexo.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")

        self.gridLayout.addWidget(self.label_sexo, 9, 1, 1, 1)

        self.label_telefono = QLabel(self.frame_3)
        self.label_telefono.setObjectName(u"label_telefono")
        self.label_telefono.setMinimumSize(QSize(191, 36))
        self.label_telefono.setMaximumSize(QSize(191, 36))
        self.label_telefono.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")

        self.gridLayout.addWidget(self.label_telefono, 2, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 8, 1, 1, 1)

        self.pbutton_cambiar_contrasenia = QPushButton(self.frame_2)
        self.pbutton_cambiar_contrasenia.setObjectName(u"pbutton_cambiar_contrasenia")
        self.pbutton_cambiar_contrasenia.setGeometry(QRect(70, 340, 181, 23))
        self.pbutton_cambiar_contrasenia.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbutton_cambiar_contrasenia.setStyleSheet(u"QPushButton{\n"
"	background-color:  rgb(255, 0, 0);\n"
"	border-radius: 10px;\n"
"	font: 14pt \"Tw Cen MT Condensed\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 208, 180);\n"
"	border-radius: 10px;\n"
"	font: 14pt \"Tw Cen MT Condensed\";\n"
"}\n"
"")
        self.frame_3.raise_()
        self.line.raise_()
        self.tbutton_noticias.raise_()
        self.tbutton_opinion.raise_()
        self.tbutton_usuario.raise_()
        self.tbutton_reserva.raise_()
        self.pbutton_cambiar_contrasenia.raise_()
        self.frame_2.raise_()
        self.frame.raise_()

        self.retranslateUi(VentanaUsuario)

        QMetaObject.connectSlotsByName(VentanaUsuario)
    # setupUi

    def retranslateUi(self, VentanaUsuario):
        VentanaUsuario.setWindowTitle(QCoreApplication.translate("VentanaUsuario", u"Usuario", None))
        self.label.setText(QCoreApplication.translate("VentanaUsuario", u"<html><head/><body><p><span style=\" color:#ffffff;\">Usuario</span></p></body></html>", None))
        self.label_2.setText("")
        self.pbutton_cerrar_sesion.setText("")
        self.tbutton_noticias.setText("")
        self.tbutton_opinion.setText("")
        self.tbutton_usuario.setText("")
        self.tbutton_reserva.setText("")
        self.label_4.setText("")
        self.label_edad.setText("")
        self.label_6.setText("")
        self.label_nombre.setText("")
        self.label_8.setText("")
        self.label_7.setText("")
        self.label_correo.setText("")
        self.label_5.setText("")
        self.label_sexo.setText("")
        self.label_telefono.setText("")
        self.pbutton_cambiar_contrasenia.setText(QCoreApplication.translate("VentanaUsuario", u"Cambiar contrase\u00f1a", None))
    # retranslateUi

