# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaOpinionesqSpIHa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import app.Vista.gui.imagenes_rc

class Ui_VentanaOpiniones(object):
    def setupUi(self, VentanaOpiniones):
        if not VentanaOpiniones.objectName():
            VentanaOpiniones.setObjectName(u"VentanaOpiniones")
        VentanaOpiniones.resize(333, 500)
        VentanaOpiniones.setMinimumSize(QSize(333, 500))
        VentanaOpiniones.setMaximumSize(QSize(333, 500))
        VentanaOpiniones.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame = QFrame(VentanaOpiniones)
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
        self.frame_2 = QFrame(VentanaOpiniones)
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
        self.tbutton_usuario = QToolButton(self.frame_2)
        self.tbutton_usuario.setObjectName(u"tbutton_usuario")
        self.tbutton_usuario.setGeometry(QRect(260, 400, 48, 30))
        self.tbutton_usuario.setMinimumSize(QSize(48, 30))
        self.tbutton_usuario.setMaximumSize(QSize(48, 30))
        self.tbutton_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.tbutton_usuario.setStyleSheet(u"background-color:rgba(0,0,0,0%);\n"
"image: url(:/imagenes/imagenes/user.png);")
        icon = QIcon()
        icon.addFile(u"../imagenes/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbutton_usuario.setIcon(icon)
        self.tbutton_usuario.setIconSize(QSize(40, 30))
        self.tbutton_noticias = QToolButton(self.frame_2)
        self.tbutton_noticias.setObjectName(u"tbutton_noticias")
        self.tbutton_noticias.setGeometry(QRect(100, 400, 48, 30))
        self.tbutton_noticias.setMinimumSize(QSize(48, 30))
        self.tbutton_noticias.setMaximumSize(QSize(48, 30))
        self.tbutton_noticias.setCursor(QCursor(Qt.PointingHandCursor))
        self.tbutton_noticias.setStyleSheet(u"background-color:rgba(0,0,0,0%);\n"
"image: url(:/imagenes/imagenes/forma.png);")
        icon1 = QIcon()
        icon1.addFile(u"../imagenes/forma.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbutton_noticias.setIcon(icon1)
        self.tbutton_noticias.setIconSize(QSize(40, 30))
        self.tbutton_reserva = QToolButton(self.frame_2)
        self.tbutton_reserva.setObjectName(u"tbutton_reserva")
        self.tbutton_reserva.setGeometry(QRect(180, 400, 48, 30))
        self.tbutton_reserva.setMinimumSize(QSize(48, 30))
        self.tbutton_reserva.setMaximumSize(QSize(48, 30))
        self.tbutton_reserva.setCursor(QCursor(Qt.PointingHandCursor))
        self.tbutton_reserva.setStyleSheet(u"background-color:rgba(0,0,0,0%);\n"
"image: url(:/imagenes/imagenes/calendar-clock.png);")
        icon2 = QIcon()
        icon2.addFile(u"../imagenes/calendar-clock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbutton_reserva.setIcon(icon2)
        self.tbutton_reserva.setIconSize(QSize(40, 30))
        self.tbutton_opinion = QToolButton(self.frame_2)
        self.tbutton_opinion.setObjectName(u"tbutton_opinion")
        self.tbutton_opinion.setGeometry(QRect(20, 370, 48, 61))
        self.tbutton_opinion.setMinimumSize(QSize(48, 33))
        self.tbutton_opinion.setCursor(QCursor(Qt.PointingHandCursor))
        self.tbutton_opinion.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius: 20px;\n"
"image: url(:/imagenes/imagenes/sobre.png);")
        icon3 = QIcon()
        icon3.addFile(u"../imagenes/sobre.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbutton_opinion.setIcon(icon3)
        self.tbutton_opinion.setIconSize(QSize(40, 30))
        self.lineedit_asunto = QLineEdit(self.frame_2)
        self.lineedit_asunto.setObjectName(u"lineedit_asunto")
        self.lineedit_asunto.setGeometry(QRect(0, -1, 333, 41))
        self.lineedit_asunto.setStyleSheet(u"border:None;")
        self.plainTextEdit_descripcion = QPlainTextEdit(self.frame_2)
        self.plainTextEdit_descripcion.setObjectName(u"plainTextEdit_descripcion")
        self.plainTextEdit_descripcion.setGeometry(QRect(0, 40, 333, 271))
        self.plainTextEdit_descripcion.setMinimumSize(QSize(333, 0))
        self.plainTextEdit_descripcion.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.plainTextEdit_descripcion.setStyleSheet(u"border:None;")
        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 30, 331, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 330, 81, 23))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
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
        self.plainTextEdit_descripcion.raise_()
        self.line.raise_()
        self.tbutton_usuario.raise_()
        self.tbutton_noticias.raise_()
        self.tbutton_reserva.raise_()
        self.tbutton_opinion.raise_()
        self.lineedit_asunto.raise_()
        self.line_2.raise_()
        self.pushButton.raise_()
        self.frame_2.raise_()
        self.frame.raise_()

        self.retranslateUi(VentanaOpiniones)

        QMetaObject.connectSlotsByName(VentanaOpiniones)
    # setupUi

    def retranslateUi(self, VentanaOpiniones):
        VentanaOpiniones.setWindowTitle(QCoreApplication.translate("VentanaOpiniones", u"Opiniones", None))
        self.label.setText(QCoreApplication.translate("VentanaOpiniones", u"<html><head/><body><p><span style=\" color:#ffffff;\">Opiniones</span></p></body></html>", None))
        self.label_2.setText("")
        self.tbutton_usuario.setText("")
        self.tbutton_noticias.setText("")
        self.tbutton_reserva.setText("")
        self.tbutton_opinion.setText("")
        self.lineedit_asunto.setPlaceholderText(QCoreApplication.translate("VentanaOpiniones", u"Asunto", None))
        self.plainTextEdit_descripcion.setDocumentTitle("")
        self.plainTextEdit_descripcion.setPlaceholderText(QCoreApplication.translate("VentanaOpiniones", u"Descripcion", None))
        self.pushButton.setText(QCoreApplication.translate("VentanaOpiniones", u"Enviar", None))
    # retranslateUi

