# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaReservaszxBWgw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import app.Vista.gui.imagenes_rc

class Ui_VentanaReservas(object):
    def setupUi(self, VentanaReservas):
        if not VentanaReservas.objectName():
            VentanaReservas.setObjectName(u"VentanaReservas")
        VentanaReservas.resize(333, 500)
        VentanaReservas.setMinimumSize(QSize(333, 500))
        VentanaReservas.setMaximumSize(QSize(333, 500))
        VentanaReservas.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame = QFrame(VentanaReservas)
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
        self.label_2.setGeometry(QRect(190, 10, 131, 41))
        self.label_2.setStyleSheet(u"image: url(:/imagenes/imagenes/logo-udemedellin-footer.png);")
        self.frame_2 = QFrame(VentanaReservas)
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
        self.tbutton_reserva = QToolButton(self.frame_2)
        self.tbutton_reserva.setObjectName(u"tbutton_reserva")
        self.tbutton_reserva.setGeometry(QRect(180, 370, 48, 61))
        self.tbutton_reserva.setMinimumSize(QSize(48, 33))
        self.tbutton_reserva.setCursor(QCursor(Qt.PointingHandCursor))
        self.tbutton_reserva.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"image: url(:/imagenes/imagenes/calendar-clock (1).png);\n"
"border-radius: 10px;\n"
"")
        icon = QIcon()
        icon.addFile(u"../imagenes/calendar-clock (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbutton_reserva.setIcon(icon)
        self.tbutton_reserva.setIconSize(QSize(40, 30))
        self.tbutton_usuario = QToolButton(self.frame_2)
        self.tbutton_usuario.setObjectName(u"tbutton_usuario")
        self.tbutton_usuario.setGeometry(QRect(260, 400, 48, 30))
        self.tbutton_usuario.setMinimumSize(QSize(48, 30))
        self.tbutton_usuario.setMaximumSize(QSize(48, 30))
        self.tbutton_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.tbutton_usuario.setStyleSheet(u"background-color:rgba(0,0,0,0%);\n"
"image: url(:/imagenes/imagenes/user.png);")
        icon1 = QIcon()
        icon1.addFile(u"../imagenes/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbutton_usuario.setIcon(icon1)
        self.tbutton_usuario.setIconSize(QSize(40, 30))
        self.tbutton_noticias = QToolButton(self.frame_2)
        self.tbutton_noticias.setObjectName(u"tbutton_noticias")
        self.tbutton_noticias.setGeometry(QRect(100, 400, 48, 30))
        self.tbutton_noticias.setMinimumSize(QSize(48, 30))
        self.tbutton_noticias.setMaximumSize(QSize(48, 30))
        self.tbutton_noticias.setCursor(QCursor(Qt.PointingHandCursor))
        self.tbutton_noticias.setStyleSheet(u"background-color:rgba(0,0,0,0%);\n"
"image: url(:/imagenes/imagenes/forma.png);")
        icon2 = QIcon()
        icon2.addFile(u"../imagenes/forma.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbutton_noticias.setIcon(icon2)
        self.tbutton_noticias.setIconSize(QSize(40, 30))
        self.tbutton_opinion = QToolButton(self.frame_2)
        self.tbutton_opinion.setObjectName(u"tbutton_opinion")
        self.tbutton_opinion.setGeometry(QRect(20, 400, 48, 30))
        self.tbutton_opinion.setMinimumSize(QSize(48, 30))
        self.tbutton_opinion.setMaximumSize(QSize(48, 30))
        self.tbutton_opinion.setCursor(QCursor(Qt.PointingHandCursor))
        self.tbutton_opinion.setStyleSheet(u"background-color:rgba(0,0,0,0%);\n"
"image: url(:/imagenes/imagenes/envelope.png);")
        icon3 = QIcon()
        icon3.addFile(u"../imagenes/envelope.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbutton_opinion.setIcon(icon3)
        self.tbutton_opinion.setIconSize(QSize(40, 30))
        self.pbutton_reservadia = QPushButton(self.frame_2)
        self.pbutton_reservadia.setObjectName(u"pbutton_reservadia")
        self.pbutton_reservadia.setGeometry(QRect(10, 80, 311, 101))
        self.pbutton_reservadia.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbutton_reservadia.setStyleSheet(u"\n"
"QPushButton{\n"
"	background-color: rgb(230, 230, 230);\n"
"	border-radius: 10px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(145, 145, 145);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(110, 130, 200, 3))
        self.line_2.setMinimumSize(QSize(200, 1))
        self.line_2.setMaximumSize(QSize(200, 16777215))
        self.line_2.setStyleSheet(u"background-color:  rgb(238, 238, 0);\n"
"border: None;\n"
"")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_diaActual = QLabel(self.frame_2)
        self.label_diaActual.setObjectName(u"label_diaActual")
        self.label_diaActual.setGeometry(QRect(20, 90, 61, 20))
        self.label_diaActual.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 14pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.label_diaActual.setAlignment(Qt.AlignCenter)
        self.label_mesActual = QLabel(self.frame_2)
        self.label_mesActual.setObjectName(u"label_mesActual")
        self.label_mesActual.setGeometry(QRect(20, 150, 61, 20))
        self.label_mesActual.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 14pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.label_mesActual.setAlignment(Qt.AlignCenter)
        self.label_fechaActual = QLabel(self.frame_2)
        self.label_fechaActual.setObjectName(u"label_fechaActual")
        self.label_fechaActual.setGeometry(QRect(20, 110, 61, 41))
        self.label_fechaActual.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 30pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.label_fechaActual.setAlignment(Qt.AlignCenter)
        self.pbutton_reservadiaSig = QPushButton(self.frame_2)
        self.pbutton_reservadiaSig.setObjectName(u"pbutton_reservadiaSig")
        self.pbutton_reservadiaSig.setGeometry(QRect(10, 220, 311, 101))
        self.pbutton_reservadiaSig.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbutton_reservadiaSig.setStyleSheet(u"\n"
"QPushButton{\n"
"	background-color: rgb(230, 230, 230);\n"
"	border-radius: 10px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(145, 145, 145);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"")
        self.label_mesSiguiente = QLabel(self.frame_2)
        self.label_mesSiguiente.setObjectName(u"label_mesSiguiente")
        self.label_mesSiguiente.setGeometry(QRect(20, 290, 61, 20))
        self.label_mesSiguiente.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 14pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.label_mesSiguiente.setAlignment(Qt.AlignCenter)
        self.label_diaSiguiente = QLabel(self.frame_2)
        self.label_diaSiguiente.setObjectName(u"label_diaSiguiente")
        self.label_diaSiguiente.setGeometry(QRect(20, 230, 61, 20))
        self.label_diaSiguiente.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 14pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.label_diaSiguiente.setAlignment(Qt.AlignCenter)
        self.label_fechaSiguiente = QLabel(self.frame_2)
        self.label_fechaSiguiente.setObjectName(u"label_fechaSiguiente")
        self.label_fechaSiguiente.setGeometry(QRect(20, 250, 61, 41))
        self.label_fechaSiguiente.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 30pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.label_fechaSiguiente.setAlignment(Qt.AlignCenter)
        self.line_3 = QFrame(self.frame_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(110, 270, 200, 3))
        self.line_3.setMinimumSize(QSize(200, 1))
        self.line_3.setMaximumSize(QSize(200, 16777215))
        self.line_3.setStyleSheet(u"background-color:  rgb(238, 238, 0);\n"
"border: None;\n"
"")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label_recuerdoDiaActual = QLabel(self.frame_2)
        self.label_recuerdoDiaActual.setObjectName(u"label_recuerdoDiaActual")
        self.label_recuerdoDiaActual.setGeometry(QRect(120, 140, 171, 31))
        self.label_recuerdoDiaActual.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 12pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.label_recuerdoDiaSiguiente = QLabel(self.frame_2)
        self.label_recuerdoDiaSiguiente.setObjectName(u"label_recuerdoDiaSiguiente")
        self.label_recuerdoDiaSiguiente.setGeometry(QRect(120, 280, 171, 31))
        self.label_recuerdoDiaSiguiente.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 12pt \"Tw Cen MT Condensed\";\n"
"border: None;")

        self.retranslateUi(VentanaReservas)

        QMetaObject.connectSlotsByName(VentanaReservas)
    # setupUi

    def retranslateUi(self, VentanaReservas):
        VentanaReservas.setWindowTitle(QCoreApplication.translate("VentanaReservas", u"Reservas", None))
        self.label.setText(QCoreApplication.translate("VentanaReservas", u"<html><head/><body><p><span style=\" color:#ffffff;\">Reservas</span></p></body></html>", None))
        self.label_2.setText("")
        self.tbutton_reserva.setText("")
        self.tbutton_usuario.setText("")
        self.tbutton_noticias.setText("")
        self.tbutton_opinion.setText("")
        self.pbutton_reservadia.setText("")
        self.label_diaActual.setText(QCoreApplication.translate("VentanaReservas", u"Lunes", None))
        self.label_mesActual.setText(QCoreApplication.translate("VentanaReservas", u"Julio", None))
        self.label_fechaActual.setText(QCoreApplication.translate("VentanaReservas", u"<html><head/><body><p><span style=\" color:#f90808;\">18</span></p></body></html>", None))
        self.pbutton_reservadiaSig.setText("")
        self.label_mesSiguiente.setText(QCoreApplication.translate("VentanaReservas", u"Julio", None))
        self.label_diaSiguiente.setText(QCoreApplication.translate("VentanaReservas", u"Martes", None))
        self.label_fechaSiguiente.setText(QCoreApplication.translate("VentanaReservas", u"<html><head/><body><p><span style=\" color:#57b400;\">19</span></p></body></html>", None))
        self.label_recuerdoDiaActual.setText("")
        self.label_recuerdoDiaSiguiente.setText("")
    # retranslateUi

