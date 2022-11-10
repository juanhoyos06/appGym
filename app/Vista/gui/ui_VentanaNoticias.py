# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaNoticiasNFoNSB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import app.Vista.gui.imagenes_rc


class Ui_VentanaNoticias(object):
    def setupUi(self, VentanaNoticias):
        if not VentanaNoticias.objectName():
            VentanaNoticias.setObjectName(u"VentanaNoticias")
        VentanaNoticias.resize(333, 500)
        VentanaNoticias.setMinimumSize(QSize(333, 500))
        VentanaNoticias.setMaximumSize(QSize(333, 500))
        VentanaNoticias.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame = QFrame(VentanaNoticias)
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
        self.frame_2 = QFrame(VentanaNoticias)
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
        self.tbutton_noticias.setGeometry(QRect(100, 370, 48, 61))
        self.tbutton_noticias.setMinimumSize(QSize(48, 33))
        self.tbutton_noticias.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"image: url(:/imagenes/imagenes/form.png);\n"
"border-radius: 20px;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../imagenes/form.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbutton_noticias.setIcon(icon1)
        self.tbutton_noticias.setIconSize(QSize(40, 30))
        self.tbutton_usuario = QToolButton(self.frame_2)
        self.tbutton_usuario.setObjectName(u"tbutton_usuario")
        self.tbutton_usuario.setGeometry(QRect(260, 400, 48, 30))
        self.tbutton_usuario.setMinimumSize(QSize(48, 30))
        self.tbutton_usuario.setMaximumSize(QSize(48, 30))
        self.tbutton_usuario.setStyleSheet(u"background-color:rgba(0,0,0,0%);\n"
"image: url(:/imagenes/imagenes/user.png);")
        icon2 = QIcon()
        icon2.addFile(u"../imagenes/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbutton_usuario.setIcon(icon2)
        self.tbutton_usuario.setIconSize(QSize(40, 30))
        self.tbutton_reservas = QToolButton(self.frame_2)
        self.tbutton_reservas.setObjectName(u"tbutton_reservas")
        self.tbutton_reservas.setGeometry(QRect(180, 400, 48, 30))
        self.tbutton_reservas.setMinimumSize(QSize(48, 30))
        self.tbutton_reservas.setMaximumSize(QSize(48, 30))
        self.tbutton_reservas.setStyleSheet(u"background-color:rgba(0,0,0,0%);\n"
"image: url(:/imagenes/imagenes/calendar-clock.png);")
        icon3 = QIcon()
        icon3.addFile(u"../imagenes/calendar-clock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbutton_reservas.setIcon(icon3)
        self.tbutton_reservas.setIconSize(QSize(40, 30))
        self.tbutton_opinion = QToolButton(self.frame_2)
        self.tbutton_opinion.setObjectName(u"tbutton_opinion")
        self.tbutton_opinion.setGeometry(QRect(20, 400, 48, 30))
        self.tbutton_opinion.setMinimumSize(QSize(48, 30))
        self.tbutton_opinion.setMaximumSize(QSize(48, 30))
        self.tbutton_opinion.setStyleSheet(u"background-color:rgba(0,0,0,0%);\n"
"image: url(:/imagenes/imagenes/envelope.png);")
        self.tbutton_opinion.setIcon(icon)
        self.tbutton_opinion.setIconSize(QSize(40, 30))
        self.frame_2.raise_()
        self.frame.raise_()

        self.retranslateUi(VentanaNoticias)

        QMetaObject.connectSlotsByName(VentanaNoticias)
    # setupUi

    def retranslateUi(self, VentanaNoticias):
        VentanaNoticias.setWindowTitle(QCoreApplication.translate("VentanaNoticias", u"Noticias", None))
        self.label.setText(QCoreApplication.translate("VentanaNoticias", u"<html><head/><body><p><span style=\" color:#ffffff;\">Noticias</span></p></body></html>", None))
        self.label_2.setText("")
        self.pbutton_cerrar_sesion.setText("")
        self.tbutton_noticias.setText("")
        self.tbutton_usuario.setText("")
        self.tbutton_reservas.setText("")
        self.tbutton_opinion.setText("")
    # retranslateUi

