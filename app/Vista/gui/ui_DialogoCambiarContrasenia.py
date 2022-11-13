# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogoCambiarContraseniaHVlpNQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2 import QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import app.Vista.gui.imagenes_rc

class Ui_DialogCambiarContrasenia(object):
    def setupUi(self, DialogCambiarContrasenia):
        if not DialogCambiarContrasenia.objectName():
            DialogCambiarContrasenia.setObjectName(u"DialogCambiarContrasenia")
        DialogCambiarContrasenia.resize(330, 328)
        DialogCambiarContrasenia.setMinimumSize(QSize(330, 328))
        DialogCambiarContrasenia.setMaximumSize(QSize(330, 328))
        self.frame_2 = QFrame(DialogCambiarContrasenia)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 61, 333, 401))
        self.frame_2.setMinimumSize(QSize(333, 401))
        self.frame_2.setMaximumSize(QSize(333, 401))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 20, 333, 191))
        self.frame_3.setMinimumSize(QSize(333, 191))
        self.frame_3.setMaximumSize(QSize(333, 191))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 20, 31, 32))
        self.label_5.setStyleSheet(u"image: url(:/imagenes/imagenes/id-insignia.png);")
        self.label_5.setPixmap(QPixmap(u"../imagenes/id-insignia.png"))
        self.label_5.setScaledContents(True)
        self.lineedit_cedula = QLineEdit(self.frame_3)
        self.lineedit_cedula.setObjectName(u"lineedit_cedula")
        self.lineedit_cedula.setValidator(QtGui.QIntValidator())
        self.lineedit_cedula.setGeometry(QRect(110, 22, 191, 36))
        self.lineedit_cedula.setMinimumSize(QSize(191, 36))
        self.lineedit_cedula.setMaximumSize(QSize(302, 36))
        self.lineedit_cedula.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")
        self.lineedit_cedula.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lineedit_contrasenia = QLineEdit(self.frame_3)
        self.lineedit_contrasenia.setObjectName(u"lineedit_contrasenia")
        self.lineedit_contrasenia.setGeometry(QRect(110, 76, 191, 36))
        self.lineedit_contrasenia.setMinimumSize(QSize(191, 36))
        self.lineedit_contrasenia.setMaximumSize(QSize(302, 36))
        self.lineedit_contrasenia.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")
        self.lineedit_contrasenia.setEchoMode(QLineEdit.Password)
        self.lineedit_recuperarContrasenia = QLineEdit(self.frame_3)
        self.lineedit_recuperarContrasenia.setObjectName(u"lineedit_recuperarContrasenia")
        self.lineedit_recuperarContrasenia.setGeometry(QRect(110, 130, 191, 36))
        self.lineedit_recuperarContrasenia.setMinimumSize(QSize(191, 36))
        self.lineedit_recuperarContrasenia.setMaximumSize(QSize(302, 36))
        self.lineedit_recuperarContrasenia.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")
        self.lineedit_recuperarContrasenia.setEchoMode(QLineEdit.Password)
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 70, 31, 41))
        self.label_7.setStyleSheet(u"image: url(:/imagenes/imagenes/bloquear.png);")
        self.label_7.setPixmap(QPixmap(u"../imagenes/id-insignia.png"))
        self.label_7.setScaledContents(True)
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 130, 31, 32))
        self.label_8.setStyleSheet(u"image: url(:/imagenes/imagenes/bloquear.png);")
        self.label_8.setPixmap(QPixmap(u"../imagenes/id-insignia.png"))
        self.label_8.setScaledContents(True)
        self.buttonBox = QDialogButtonBox(self.frame_2)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(0, 220, 341, 31))
        self.buttonBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonBox.setStyleSheet(u"QPushButton{\n"
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
"}")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.frame = QFrame(DialogCambiarContrasenia)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 333, 61))
        self.frame.setMinimumSize(QSize(333, 51))
        self.frame.setStyleSheet(u"background-color:  rgb(255, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 151, 41))
        self.label.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 16pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(182, 10, 141, 41))
        self.label_2.setStyleSheet(u"image: url(:/imagenes/imagenes/logo-udemedellin-footer.png);")
        self.label_2.setPixmap(QPixmap(u"../imagenes/logo-udemedellin-footer.png"))
        self.label_2.setScaledContents(True)

        self.retranslateUi(DialogCambiarContrasenia)
        self.buttonBox.accepted.connect(DialogCambiarContrasenia.accept)
        self.buttonBox.rejected.connect(DialogCambiarContrasenia.reject)

        QMetaObject.connectSlotsByName(DialogCambiarContrasenia)
    # setupUi

    def retranslateUi(self, DialogCambiarContrasenia):
        DialogCambiarContrasenia.setWindowTitle(QCoreApplication.translate("DialogCambiarContrasenia", u"Cambiar Contrase\u00f1a", None))
        self.label_5.setText("")
        self.lineedit_cedula.setPlaceholderText(QCoreApplication.translate("DialogCambiarContrasenia", u"  Cedula ", None))
        self.lineedit_contrasenia.setPlaceholderText(QCoreApplication.translate("DialogCambiarContrasenia", u"  Nueva Contrase\u00f1a", None))
        self.lineedit_recuperarContrasenia.setPlaceholderText(QCoreApplication.translate("DialogCambiarContrasenia", u"  Confirmar contrase\u00f1a", None))
        self.label_7.setText("")
        self.label_8.setText("")
        self.label.setText(QCoreApplication.translate("DialogCambiarContrasenia", u"<html><head/><body><p><span style=\" color:#ffffff;\">Cambiar contrase\u00f1a</span></p></body></html>", None))
        self.label_2.setText("")
    # retranslateUi

