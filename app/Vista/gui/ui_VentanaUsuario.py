# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaUsuariokYYSRD.ui'
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
        self.label.setGeometry(QRect(10, 10, 91, 41))
        self.label.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 20pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(182, 10, 141, 41))
        self.label_2.setStyleSheet(u"image: url(:/imagenes/imagenes/logo-udemedellin-footer.png);")
        self.label_2.setPixmap(QPixmap(u"../imagenes/logo-udemedellin-footer.png"))
        self.label_2.setScaledContents(True)
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
        icon = QIcon()
        icon.addFile(u"../imagenes/forma.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbutton_noticias.setIcon(icon)
        self.tbutton_noticias.setIconSize(QSize(40, 30))
        self.tbutton_opinion = QToolButton(self.frame_2)
        self.tbutton_opinion.setObjectName(u"tbutton_opinion")
        self.tbutton_opinion.setGeometry(QRect(20, 400, 48, 30))
        self.tbutton_opinion.setMinimumSize(QSize(48, 30))
        self.tbutton_opinion.setMaximumSize(QSize(48, 30))
        self.tbutton_opinion.setCursor(QCursor(Qt.PointingHandCursor))
        self.tbutton_opinion.setStyleSheet(u"background-color:rgba(0,0,0,0%);\n"
"image: url(:/imagenes/imagenes/envelope.png);")
        icon1 = QIcon()
        icon1.addFile(u"../imagenes/envelope.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbutton_opinion.setIcon(icon1)
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
        self.frame_3.setGeometry(QRect(0, 50, 333, 241))
        self.frame_3.setMinimumSize(QSize(333, 241))
        self.frame_3.setMaximumSize(QSize(333, 241))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.lineedit_nombre = QLineEdit(self.frame_3)
        self.lineedit_nombre.setObjectName(u"lineedit_nombre")
        self.lineedit_nombre.setGeometry(QRect(110, 8, 191, 36))
        self.lineedit_nombre.setMinimumSize(QSize(191, 36))
        self.lineedit_nombre.setMaximumSize(QSize(302, 36))
        self.lineedit_nombre.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")
        self.lineedit_nombre.setCursorPosition(0)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 62, 31, 32))
        self.label_4.setStyleSheet(u"image: url(:/imagenes/imagenes/circle-phone-flip.png);")
        self.label_4.setPixmap(QPixmap(u"../imagenes/circle-phone-flip.png"))
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 116, 31, 32))
        self.label_5.setStyleSheet(u"image: url(:/imagenes/imagenes/id-insignia.png);")
        self.label_5.setPixmap(QPixmap(u"../imagenes/id-insignia.png"))
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 170, 31, 31))
        self.label_6.setStyleSheet(u"image: url(:/imagenes/imagenes/sobre (2).png);")
        self.label_6.setPixmap(QPixmap(u"../imagenes/sobre (2).png"))
        self.label_6.setScaledContents(True)
        self.lineedit_telefono = QLineEdit(self.frame_3)
        self.lineedit_telefono.setObjectName(u"lineedit_telefono")
        self.lineedit_telefono.setGeometry(QRect(110, 62, 191, 36))
        self.lineedit_telefono.setMinimumSize(QSize(191, 36))
        self.lineedit_telefono.setMaximumSize(QSize(302, 36))
        self.lineedit_telefono.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")
        self.lineedit_cedula = QLineEdit(self.frame_3)
        self.lineedit_cedula.setObjectName(u"lineedit_cedula")
        self.lineedit_cedula.setGeometry(QRect(110, 116, 191, 36))
        self.lineedit_cedula.setMinimumSize(QSize(191, 36))
        self.lineedit_cedula.setMaximumSize(QSize(302, 36))
        self.lineedit_cedula.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")
        self.lineedit_correo = QLineEdit(self.frame_3)
        self.lineedit_correo.setObjectName(u"lineedit_correo")
        self.lineedit_correo.setGeometry(QRect(110, 170, 191, 36))
        self.lineedit_correo.setMinimumSize(QSize(191, 36))
        self.lineedit_correo.setMaximumSize(QSize(302, 36))
        self.lineedit_correo.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 8, 31, 32))
        self.label_7.setStyleSheet(u"image: url(:/imagenes/imagenes/usuario.png);")
        self.label_7.setPixmap(QPixmap(u"../imagenes/usuario.png"))
        self.label_7.setScaledContents(True)
        self.pbutton_guardar = QPushButton(self.frame_2)
        self.pbutton_guardar.setObjectName(u"pbutton_guardar")
        self.pbutton_guardar.setGeometry(QRect(70, 300, 181, 23))
        self.pbutton_guardar.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbutton_guardar.setStyleSheet(u"QPushButton{\n"
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
        self.pbutton_guardar.raise_()
        self.frame_2.raise_()
        self.frame.raise_()

        self.retranslateUi(VentanaUsuario)

        QMetaObject.connectSlotsByName(VentanaUsuario)
    # setupUi

    def retranslateUi(self, VentanaUsuario):
        VentanaUsuario.setWindowTitle(QCoreApplication.translate("VentanaUsuario", u"Usuario", None))
        self.label.setText(QCoreApplication.translate("VentanaUsuario", u"<html><head/><body><p><span style=\" color:#ffffff;\">Usuario</span></p></body></html>", None))
        self.label_2.setText("")
        self.tbutton_noticias.setText("")
        self.tbutton_opinion.setText("")
        self.tbutton_usuario.setText("")
        self.tbutton_reserva.setText("")
        self.lineedit_nombre.setPlaceholderText(QCoreApplication.translate("VentanaUsuario", u"  Nombre", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.lineedit_telefono.setPlaceholderText(QCoreApplication.translate("VentanaUsuario", u"  Telefono", None))
        self.lineedit_cedula.setPlaceholderText(QCoreApplication.translate("VentanaUsuario", u"  Cedula", None))
        self.lineedit_correo.setPlaceholderText(QCoreApplication.translate("VentanaUsuario", u"  Correo", None))
        self.label_7.setText("")
        self.pbutton_guardar.setText(QCoreApplication.translate("VentanaUsuario", u"Guardar", None))
    # retranslateUi

