# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaDeInicioJGSYtL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import app.Vista.gui.imagenes_rc

class Ui_VentanaDeInicio(object):
    def setupUi(self, VentanaDeInicio):
        if not VentanaDeInicio.objectName():
            VentanaDeInicio.setObjectName(u"VentanaDeInicio")
        VentanaDeInicio.resize(333, 500)
        VentanaDeInicio.setMaximumSize(QSize(333, 500))
        VentanaDeInicio.setIconSize(QSize(24, 24))
        self.centralwidget = QWidget(VentanaDeInicio)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setGeometry(QRect(0, 0, 333, 500))
        self.frame.setMinimumSize(QSize(333, 500))
        self.frame.setMaximumSize(QSize(333, 500))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"border: 1px solid #000")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_iniciarSesion = QLabel(self.frame)
        self.label_iniciarSesion.setObjectName(u"label_iniciarSesion")
        self.label_iniciarSesion.setEnabled(False)
        self.label_iniciarSesion.setGeometry(QRect(50, 170, 121, 21))
        self.label_iniciarSesion.setMinimumSize(QSize(121, 21))
        self.label_iniciarSesion.setMaximumSize(QSize(121, 21))
        font = QFont()
        font.setFamily(u"Tw Cen MT Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.label_iniciarSesion.setFont(font)
        self.label_iniciarSesion.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 14pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.label_iniciarSesion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pbutton_salir = QPushButton(self.frame)
        self.pbutton_salir.setObjectName(u"pbutton_salir")
        self.pbutton_salir.setEnabled(True)
        self.pbutton_salir.setGeometry(QRect(90, 410, 75, 23))
        self.pbutton_salir.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbutton_salir.setStyleSheet(u"\n"
"\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(255, 0, 0);\n"
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
"\n"
"}")
        self.pbutton_ingresar = QPushButton(self.frame)
        self.pbutton_ingresar.setObjectName(u"pbutton_ingresar")
        self.pbutton_ingresar.setGeometry(QRect(170, 410, 81, 23))
        self.pbutton_ingresar.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbutton_ingresar.setStyleSheet(u"QPushButton{\n"
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
"\n"
"")
        self.pbutton_ingresar.setCheckable(False)
        self.lineedit_usuario = QLineEdit(self.frame)
        self.lineedit_usuario.setObjectName(u"lineedit_usuario")
        self.lineedit_usuario.setGeometry(QRect(50, 210, 241, 31))
        self.lineedit_usuario.setMinimumSize(QSize(241, 31))
        self.lineedit_usuario.setMaximumSize(QSize(241, 31))
        self.lineedit_usuario.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"border:None;\n"
"font: 14pt \"Tw Cen MT Condensed\";")
        self.lineedit_usuario.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineedit_usuario.setDragEnabled(False)
        self.lineedit_usuario.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineedit_contrasenia = QLineEdit(self.frame)
        self.lineedit_contrasenia.setObjectName(u"lineedit_contrasenia")
        self.lineedit_contrasenia.setGeometry(QRect(50, 270, 241, 31))
        self.lineedit_contrasenia.setMinimumSize(QSize(241, 31))
        self.lineedit_contrasenia.setMaximumSize(QSize(241, 31))
        self.lineedit_contrasenia.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"border:None;\n"
"font: 14pt \"Tw Cen MT Condensed\";")
        self.lineedit_contrasenia.setEchoMode(QLineEdit.Password)
        self.lineedit_contrasenia.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pbutton_recuperarContrasenia = QPushButton(self.frame)
        self.pbutton_recuperarContrasenia.setObjectName(u"pbutton_recuperarContrasenia")
        self.pbutton_recuperarContrasenia.setGeometry(QRect(50, 320, 131, 23))
        self.pbutton_recuperarContrasenia.setMinimumSize(QSize(131, 23))
        self.pbutton_recuperarContrasenia.setMaximumSize(QSize(131, 23))
        font1 = QFont()
        font1.setFamily(u"Tw Cen MT Condensed")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(True)
        font1.setWeight(50)
        self.pbutton_recuperarContrasenia.setFont(font1)
        self.pbutton_recuperarContrasenia.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbutton_recuperarContrasenia.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"font: 14pt \"Tw Cen MT Condensed\";\n"
"selection-color: rgb(74, 199, 36);\n"
"border: None;\n"
"")
        self.pbutton_crearCuenta = QPushButton(self.frame)
        self.pbutton_crearCuenta.setObjectName(u"pbutton_crearCuenta")
        self.pbutton_crearCuenta.setGeometry(QRect(50, 350, 101, 23))
        self.pbutton_crearCuenta.setMinimumSize(QSize(0, 23))
        self.pbutton_crearCuenta.setMaximumSize(QSize(131, 23))
        self.pbutton_crearCuenta.setFont(font1)
        self.pbutton_crearCuenta.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbutton_crearCuenta.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"font: 14pt \"Tw Cen MT Condensed\";\n"
"selection-color: rgb(74, 199, 36);\n"
"border: None;\n"
"")
        self.pbutton_crearCuenta.setAutoRepeatInterval(103)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 291, 131))
        self.label.setStyleSheet(u"image: url(:/imagenes/imagenes/logo_udemedellin2.png);\n"
"")
        VentanaDeInicio.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaDeInicio)
        self.pbutton_salir.clicked.connect(VentanaDeInicio.close)

        self.pbutton_ingresar.setDefault(False)


        QMetaObject.connectSlotsByName(VentanaDeInicio)
    # setupUi

    def retranslateUi(self, VentanaDeInicio):
        VentanaDeInicio.setWindowTitle(QCoreApplication.translate("VentanaDeInicio", u"Login AppGym", None))
        self.label_iniciarSesion.setText(QCoreApplication.translate("VentanaDeInicio", u"<html><head/><body><p><span style=\" color:#000000;\">Iniciar sesion </span></p></body></html>", None))
        self.pbutton_salir.setText(QCoreApplication.translate("VentanaDeInicio", u"Salir", None))
        self.pbutton_ingresar.setText(QCoreApplication.translate("VentanaDeInicio", u"Ingresar", None))
        self.lineedit_usuario.setPlaceholderText(QCoreApplication.translate("VentanaDeInicio", u"   Usuario", None))
        self.lineedit_contrasenia.setPlaceholderText(QCoreApplication.translate("VentanaDeInicio", u"   Contrase\u00f1a", None))
        self.pbutton_recuperarContrasenia.setText(QCoreApplication.translate("VentanaDeInicio", u"Recuperar contrase\u00f1a", None))
        self.pbutton_crearCuenta.setText(QCoreApplication.translate("VentanaDeInicio", u"Crear una cuenta", None))
        self.label.setText("")
    # retranslateUi

