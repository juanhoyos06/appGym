# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaTurnoOkdWOS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import app.Vista.gui.imagenes_rc

class Ui_VentanaTurno(object):
    def setupUi(self, VentanaTurno):
        if not VentanaTurno.objectName():
            VentanaTurno.setObjectName(u"VentanaTurno")
        VentanaTurno.resize(333, 500)
        VentanaTurno.setMinimumSize(QSize(333, 500))
        VentanaTurno.setMaximumSize(QSize(333, 500))
        VentanaTurno.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame = QFrame(VentanaTurno)
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
        self.frame_2 = QFrame(VentanaTurno)
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
        self.tbutton_reserva.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius: 20px;\n"
"\n"
"image: url(:/imagenes/imagenes/calendar-clock (1).png);")
        icon = QIcon()
        icon.addFile(u"../imagenes/calendar-clock (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbutton_reserva.setIcon(icon)
        self.tbutton_reserva.setIconSize(QSize(40, 30))
        self.tbutton_usuario = QToolButton(self.frame_2)
        self.tbutton_usuario.setObjectName(u"tbutton_usuario")
        self.tbutton_usuario.setGeometry(QRect(260, 400, 48, 30))
        self.tbutton_usuario.setMinimumSize(QSize(48, 30))
        self.tbutton_usuario.setMaximumSize(QSize(48, 30))
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
        self.tbutton_opinion.setStyleSheet(u"background-color:rgba(0,0,0,0%);\n"
"image: url(:/imagenes/imagenes/envelope.png);")
        icon3 = QIcon()
        icon3.addFile(u"../imagenes/envelope.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbutton_opinion.setIcon(icon3)
        self.tbutton_opinion.setIconSize(QSize(40, 30))
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 331, 391))
        self.scrollArea.setStyleSheet(u"/*VERTICAL SCROLL*/\n"
"\n"
"QScrollBar:vertical{\n"
"	border: None;\n"
"	\n"
"	background-color: rgb(216, 216, 216);\n"
"	width: 14px;\n"
"	margin: 15px o 15px 0;\n"
"	border-radius: 0px;\n"
"}\n"
"")
        self.scrollArea.setFrameShape(QFrame.StyledPanel)
        self.scrollArea.setFrameShadow(QFrame.Raised)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 315, 389))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pbutton_turno1 = QPushButton(self.widget)
        self.pbutton_turno1.setObjectName(u"pbutton_turno1")
        self.pbutton_turno1.setGeometry(QRect(0, 40, 300, 41))
        self.pbutton_turno1.setMinimumSize(QSize(300, 0))
        self.pbutton_turno1.setMaximumSize(QSize(300, 16777215))
        self.pbutton_turno1.setFocusPolicy(Qt.StrongFocus)
        self.pbutton_turno1.setLayoutDirection(Qt.RightToLeft)
        self.pbutton_turno1.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(230, 230, 230);\n"
"	border-radius: 10px;\n"
"	font: 14pt \"Tw Cen MT Condensed\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	border-radius: 10px;\n"
"	font: 14pt \"Tw Cen MT Condensed\";\n"
"}")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 50, 121, 21))
        self.label_3.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 14pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.label_turno2 = QLabel(self.widget)
        self.label_turno2.setObjectName(u"label_turno2")
        self.label_turno2.setGeometry(QRect(160, 110, 121, 21))
        self.label_turno2.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 14pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.pbutton_turno2 = QPushButton(self.widget)
        self.pbutton_turno2.setObjectName(u"pbutton_turno2")
        self.pbutton_turno2.setGeometry(QRect(0, 100, 300, 41))
        self.pbutton_turno2.setMinimumSize(QSize(300, 0))
        self.pbutton_turno2.setMaximumSize(QSize(300, 16777215))
        self.pbutton_turno2.setFocusPolicy(Qt.StrongFocus)
        self.pbutton_turno2.setLayoutDirection(Qt.RightToLeft)
        self.pbutton_turno2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(230, 230, 230);\n"
"	border-radius: 10px;\n"
"	font: 14pt \"Tw Cen MT Condensed\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	border-radius: 10px;\n"
"	font: 14pt \"Tw Cen MT Condensed\";\n"
"}")
        self.label_turno3 = QLabel(self.widget)
        self.label_turno3.setObjectName(u"label_turno3")
        self.label_turno3.setGeometry(QRect(160, 170, 121, 21))
        self.label_turno3.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 14pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.pbutton_turno3 = QPushButton(self.widget)
        self.pbutton_turno3.setObjectName(u"pbutton_turno3")
        self.pbutton_turno3.setGeometry(QRect(0, 160, 300, 41))
        self.pbutton_turno3.setMinimumSize(QSize(300, 0))
        self.pbutton_turno3.setMaximumSize(QSize(300, 16777215))
        self.pbutton_turno3.setFocusPolicy(Qt.StrongFocus)
        self.pbutton_turno3.setLayoutDirection(Qt.RightToLeft)
        self.pbutton_turno3.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(230, 230, 230);\n"
"	border-radius: 10px;\n"
"	font: 14pt \"Tw Cen MT Condensed\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	border-radius: 10px;\n"
"	font: 14pt \"Tw Cen MT Condensed\";\n"
"}")
        self.label_turno4 = QLabel(self.widget)
        self.label_turno4.setObjectName(u"label_turno4")
        self.label_turno4.setGeometry(QRect(160, 230, 121, 21))
        self.label_turno4.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 14pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.pbutton_turno4 = QPushButton(self.widget)
        self.pbutton_turno4.setObjectName(u"pbutton_turno4")
        self.pbutton_turno4.setGeometry(QRect(0, 220, 300, 41))
        self.pbutton_turno4.setMinimumSize(QSize(300, 0))
        self.pbutton_turno4.setMaximumSize(QSize(300, 16777215))
        self.pbutton_turno4.setFocusPolicy(Qt.StrongFocus)
        self.pbutton_turno4.setLayoutDirection(Qt.RightToLeft)
        self.pbutton_turno4.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(230, 230, 230);\n"
"	border-radius: 10px;\n"
"	font: 14pt \"Tw Cen MT Condensed\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	border-radius: 10px;\n"
"	font: 14pt \"Tw Cen MT Condensed\";\n"
"}")
        self.label_turno5 = QLabel(self.widget)
        self.label_turno5.setObjectName(u"label_turno5")
        self.label_turno5.setGeometry(QRect(160, 290, 121, 21))
        self.label_turno5.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 14pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.pbutton_turno5 = QPushButton(self.widget)
        self.pbutton_turno5.setObjectName(u"pbutton_turno5")
        self.pbutton_turno5.setGeometry(QRect(0, 280, 300, 41))
        self.pbutton_turno5.setMinimumSize(QSize(300, 0))
        self.pbutton_turno5.setMaximumSize(QSize(300, 16777215))
        self.pbutton_turno5.setFocusPolicy(Qt.StrongFocus)
        self.pbutton_turno5.setLayoutDirection(Qt.RightToLeft)
        self.pbutton_turno5.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(230, 230, 230);\n"
"	border-radius: 10px;\n"
"	font: 14pt \"Tw Cen MT Condensed\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	border-radius: 10px;\n"
"	font: 14pt \"Tw Cen MT Condensed\";\n"
"}")
        self.label_turno6 = QLabel(self.widget)
        self.label_turno6.setObjectName(u"label_turno6")
        self.label_turno6.setGeometry(QRect(160, 350, 121, 21))
        self.label_turno6.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 14pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.pbutton_turno6 = QPushButton(self.widget)
        self.pbutton_turno6.setObjectName(u"pbutton_turno6")
        self.pbutton_turno6.setGeometry(QRect(0, 340, 300, 41))
        self.pbutton_turno6.setMinimumSize(QSize(300, 0))
        self.pbutton_turno6.setMaximumSize(QSize(300, 16777215))
        self.pbutton_turno6.setFocusPolicy(Qt.StrongFocus)
        self.pbutton_turno6.setLayoutDirection(Qt.RightToLeft)
        self.pbutton_turno6.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(230, 230, 230);\n"
"	border-radius: 10px;\n"
"	font: 14pt \"Tw Cen MT Condensed\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	border-radius: 10px;\n"
"	font: 14pt \"Tw Cen MT Condensed\";\n"
"}")
        self.pbutton_turno7 = QPushButton(self.widget)
        self.pbutton_turno7.setObjectName(u"pbutton_turno7")
        self.pbutton_turno7.setGeometry(QRect(0, 400, 300, 41))
        self.pbutton_turno7.setMinimumSize(QSize(300, 0))
        self.pbutton_turno7.setMaximumSize(QSize(300, 16777215))
        self.pbutton_turno7.setFocusPolicy(Qt.StrongFocus)
        self.pbutton_turno7.setLayoutDirection(Qt.RightToLeft)
        self.pbutton_turno7.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(230, 230, 230);\n"
"	border-radius: 10px;\n"
"	font: 14pt \"Tw Cen MT Condensed\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	border-radius: 10px;\n"
"	font: 14pt \"Tw Cen MT Condensed\";\n"
"}")
        self.label_turno7 = QLabel(self.widget)
        self.label_turno7.setObjectName(u"label_turno7")
        self.label_turno7.setGeometry(QRect(160, 410, 121, 21))
        self.label_turno7.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 14pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.pbutton_turno2.raise_()
        self.pbutton_turno3.raise_()
        self.pbutton_turno4.raise_()
        self.pbutton_turno5.raise_()
        self.pbutton_turno6.raise_()
        self.pbutton_turno1.raise_()
        self.label_3.raise_()
        self.label_turno2.raise_()
        self.label_turno3.raise_()
        self.label_turno4.raise_()
        self.label_turno5.raise_()
        self.label_turno6.raise_()
        self.pbutton_turno7.raise_()
        self.label_turno7.raise_()

        self.verticalLayout.addWidget(self.widget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.raise_()
        self.line.raise_()
        self.tbutton_reserva.raise_()
        self.tbutton_usuario.raise_()
        self.tbutton_noticias.raise_()
        self.tbutton_opinion.raise_()
        self.frame_2.raise_()
        self.frame.raise_()

        self.retranslateUi(VentanaTurno)

        QMetaObject.connectSlotsByName(VentanaTurno)
    # setupUi

    def retranslateUi(self, VentanaTurno):
        VentanaTurno.setWindowTitle(QCoreApplication.translate("VentanaTurno", u"Turnos ", None))
        self.label.setText(QCoreApplication.translate("VentanaTurno", u"<html><head/><body><p><span style=\" color:#ffffff;\">Reservas</span></p></body></html>", None))
        self.label_2.setText("")
        self.tbutton_reserva.setText("")
        self.tbutton_usuario.setText("")
        self.tbutton_noticias.setText("")
        self.tbutton_opinion.setText("")
        self.pbutton_turno1.setText(QCoreApplication.translate("VentanaTurno", u"6:00 AM - 8:00 AM                                                            ", None))
        self.label_3.setText("")
        self.label_turno2.setText("")
        self.pbutton_turno2.setText(QCoreApplication.translate("VentanaTurno", u"8:00 AM - 10:00 AM                                                            ", None))
        self.label_turno3.setText("")
        self.pbutton_turno3.setText(QCoreApplication.translate("VentanaTurno", u"10:00 AM - 12:00 AM                                                            ", None))
        self.label_turno4.setText("")
        self.pbutton_turno4.setText(QCoreApplication.translate("VentanaTurno", u"12:00 PM - 2:00 PM                                                            ", None))
        self.label_turno5.setText("")
        self.pbutton_turno5.setText(QCoreApplication.translate("VentanaTurno", u"2:00 PM - 4:00 PM                                                            ", None))
        self.label_turno6.setText("")
        self.pbutton_turno6.setText(QCoreApplication.translate("VentanaTurno", u"4:00 PM - 6:00 PM                                                            ", None))
        self.pbutton_turno7.setText(QCoreApplication.translate("VentanaTurno", u"6:00 PM - 8:00 PM                                                            ", None))
        self.label_turno7.setText("")
    # retranslateUi
