# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogoCrearUsuarioHXNNtC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


import app.Vista.gui.imagenes_rc

class Ui_DialogoCrearUsuario(object):
    def setupUi(self, DialogoCrearUsuario):
        if not DialogoCrearUsuario.objectName():
            DialogoCrearUsuario.setObjectName(u"DialogoCrearUsuario")
        DialogoCrearUsuario.resize(333, 500)
        DialogoCrearUsuario.setMinimumSize(QSize(333, 500))
        DialogoCrearUsuario.setMaximumSize(QSize(333, 500))
        DialogoCrearUsuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.buttonBox = QDialogButtonBox(DialogoCrearUsuario)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(-20, 460, 341, 32))
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
        self.frame = QFrame(DialogoCrearUsuario)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 333, 61))
        self.frame.setMinimumSize(QSize(333, 61))
        self.frame.setMaximumSize(QSize(333, 61))
        self.frame.setStyleSheet(u"background-color:  rgb(255, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(182, 10, 141, 41))
        self.label_2.setStyleSheet(u"image: url(:/imagenes/imagenes/logo-udemedellin-footer.png);")
        self.label_2.setPixmap(QPixmap(u"../imagenes/logo-udemedellin-footer.png"))
        self.label_2.setScaledContents(True)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 121, 41))
        self.label.setMinimumSize(QSize(121, 41))
        self.label.setMaximumSize(QSize(121, 41))
        self.label.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 20pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.scrollArea = QScrollArea(DialogoCrearUsuario)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 60, 331, 391))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -192, 312, 581))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(31, 32))
        self.label_8.setStyleSheet(u"image: url(:/imagenes/imagenes/id-insignia.png);")
        self.label_8.setPixmap(QPixmap(u"../imagenes/id-insignia.png"))
        self.label_8.setScaledContents(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.lineedit_cedula_3 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineedit_cedula_3.setObjectName(u"lineedit_cedula_3")
        self.lineedit_cedula_3.setMinimumSize(QSize(191, 36))
        self.lineedit_cedula_3.setMaximumSize(QSize(302, 36))
        self.lineedit_cedula_3.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")
        self.lineedit_cedula_3.setCursorPosition(0)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineedit_cedula_3)

        self.verticalSpacer = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(1, QFormLayout.FieldRole, self.verticalSpacer)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(31, 32))
        self.label_12.setStyleSheet(u"image: url(:/imagenes/imagenes/usuario.png);")
        self.label_12.setPixmap(QPixmap(u"../imagenes/usuario.png"))
        self.label_12.setScaledContents(True)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_12)

        self.lineedit_nombre = QLineEdit(self.scrollAreaWidgetContents)
        self.lineedit_nombre.setObjectName(u"lineedit_nombre")
        self.lineedit_nombre.setMinimumSize(QSize(191, 36))
        self.lineedit_nombre.setMaximumSize(QSize(302, 36))
        self.lineedit_nombre.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineedit_nombre)

        self.verticalSpacer_2 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(3, QFormLayout.FieldRole, self.verticalSpacer_2)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(31, 32))
        self.label_4.setStyleSheet(u"image: url(:/imagenes/imagenes/circle-phone-flip.png);")
        self.label_4.setPixmap(QPixmap(u"../imagenes/circle-phone-flip.png"))
        self.label_4.setScaledContents(True)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.lineedit_telefono = QLineEdit(self.scrollAreaWidgetContents)
        self.lineedit_telefono.setObjectName(u"lineedit_telefono")
        self.lineedit_telefono.setMinimumSize(QSize(191, 36))
        self.lineedit_telefono.setMaximumSize(QSize(302, 36))
        self.lineedit_telefono.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineedit_telefono)

        self.verticalSpacer_3 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(5, QFormLayout.FieldRole, self.verticalSpacer_3)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(31, 32))
        self.label_6.setStyleSheet(u"image: url(:/imagenes/imagenes/sobre (2).png);")
        self.label_6.setPixmap(QPixmap(u"../imagenes/sobre (2).png"))
        self.label_6.setScaledContents(True)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_6)

        self.lineedit_correo = QLineEdit(self.scrollAreaWidgetContents)
        self.lineedit_correo.setObjectName(u"lineedit_correo")
        self.lineedit_correo.setMinimumSize(QSize(191, 36))
        self.lineedit_correo.setMaximumSize(QSize(302, 36))
        self.lineedit_correo.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineedit_correo)

        self.verticalSpacer_4 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(7, QFormLayout.FieldRole, self.verticalSpacer_4)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(31, 32))
        self.label_13.setStyleSheet(u"image: url(:/imagenes/imagenes/age-group (1).png);")
        self.label_13.setPixmap(QPixmap(u"../imagenes/sobre (2).png"))
        self.label_13.setScaledContents(True)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_13)

        self.lineedit_edad = QLineEdit(self.scrollAreaWidgetContents)
        self.lineedit_edad.setObjectName(u"lineedit_edad")
        self.lineedit_edad.setMinimumSize(QSize(191, 36))
        self.lineedit_edad.setMaximumSize(QSize(302, 36))
        self.lineedit_edad.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineedit_edad)

        self.verticalSpacer_5 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(9, QFormLayout.FieldRole, self.verticalSpacer_5)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(31, 32))
        self.label_14.setStyleSheet(u"image: url(:/imagenes/imagenes/genero.png);")
        self.label_14.setPixmap(QPixmap(u"../imagenes/sobre (2).png"))
        self.label_14.setScaledContents(True)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_14)

        self.comboBox_genero = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_genero.setObjectName(u"comboBox_genero")
        self.comboBox_genero.setMinimumSize(QSize(0, 32))
        self.comboBox_genero.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.comboBox_genero)

        self.verticalSpacer_6 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(11, QFormLayout.FieldRole, self.verticalSpacer_6)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(31, 32))
        self.label_3.setStyleSheet(u"image: url(:/imagenes/imagenes/bloquear.png);")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_3)

        self.lineedit_contrasenia = QLineEdit(self.scrollAreaWidgetContents)
        self.lineedit_contrasenia.setObjectName(u"lineedit_contrasenia")
        self.lineedit_contrasenia.setMinimumSize(QSize(191, 36))
        self.lineedit_contrasenia.setMaximumSize(QSize(302, 36))
        self.lineedit_contrasenia.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")
        self.lineedit_contrasenia.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.lineedit_contrasenia)

        self.verticalSpacer_7 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(14, QFormLayout.FieldRole, self.verticalSpacer_7)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(31, 32))
        self.label_5.setStyleSheet(u"image: url(:/imagenes/imagenes/bloquear.png);")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.label_5)

        self.lineedit_verificar_contrasenia = QLineEdit(self.scrollAreaWidgetContents)
        self.lineedit_verificar_contrasenia.setObjectName(u"lineedit_verificar_contrasenia")
        self.lineedit_verificar_contrasenia.setMinimumSize(QSize(191, 36))
        self.lineedit_verificar_contrasenia.setMaximumSize(QSize(302, 36))
        self.lineedit_verificar_contrasenia.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")
        self.lineedit_verificar_contrasenia.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.lineedit_verificar_contrasenia)

        self.verticalSpacer_8 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(16, QFormLayout.FieldRole, self.verticalSpacer_8)

        self.checkBox_estudiante = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_estudiante.setObjectName(u"checkBox_estudiante")

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.checkBox_estudiante)

        self.checkBox_egresado = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_egresado.setObjectName(u"checkBox_egresado")

        self.formLayout.setWidget(18, QFormLayout.FieldRole, self.checkBox_egresado)

        self.checkBox_otro = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_otro.setObjectName(u"checkBox_otro")

        self.formLayout.setWidget(19, QFormLayout.FieldRole, self.checkBox_otro)

        self.verticalSpacer_9 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(20, QFormLayout.FieldRole, self.verticalSpacer_9)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(31, 32))
        self.label_7.setStyleSheet(u"image: url(:/imagenes/imagenes/lista-de-verificacion.png);")

        self.formLayout.setWidget(21, QFormLayout.LabelRole, self.label_7)

        self.lineedit_programa = QLineEdit(self.scrollAreaWidgetContents)
        self.lineedit_programa.setObjectName(u"lineedit_programa")
        self.lineedit_programa.setMinimumSize(QSize(191, 36))
        self.lineedit_programa.setMaximumSize(QSize(302, 36))
        self.lineedit_programa.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"border-radius: 10px;")
        self.lineedit_programa.setEchoMode(QLineEdit.Normal)

        self.formLayout.setWidget(21, QFormLayout.FieldRole, self.lineedit_programa)

        self.verticalSpacer_10 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(22, QFormLayout.FieldRole, self.verticalSpacer_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(DialogoCrearUsuario)
        self.buttonBox.accepted.connect(DialogoCrearUsuario.accept)
        self.buttonBox.rejected.connect(DialogoCrearUsuario.reject)

        QMetaObject.connectSlotsByName(DialogoCrearUsuario)
    # setupUi

    def retranslateUi(self, DialogoCrearUsuario):
        DialogoCrearUsuario.setWindowTitle(QCoreApplication.translate("DialogoCrearUsuario", u"Crear usuario", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("DialogoCrearUsuario", u"<html><head/><body><p><span style=\" color:#ffffff;\">Crear usuario</span></p><p><br/></p></body></html>", None))
        self.label_8.setText("")
        self.lineedit_cedula_3.setPlaceholderText(QCoreApplication.translate("DialogoCrearUsuario", u"  C\u00e9dula", None))
        self.label_12.setText("")
        self.lineedit_nombre.setPlaceholderText(QCoreApplication.translate("DialogoCrearUsuario", u"  Nombre", None))
        self.label_4.setText("")
        self.lineedit_telefono.setPlaceholderText(QCoreApplication.translate("DialogoCrearUsuario", u"  Tel\u00e9fono", None))
        self.label_6.setText("")
        self.lineedit_correo.setPlaceholderText(QCoreApplication.translate("DialogoCrearUsuario", u"  Correo", None))
        self.label_13.setText("")
        self.lineedit_edad.setPlaceholderText(QCoreApplication.translate("DialogoCrearUsuario", u"  Edad", None))
        self.label_14.setText("")
        self.label_3.setText("")
        self.lineedit_contrasenia.setPlaceholderText(QCoreApplication.translate("DialogoCrearUsuario", u"  Contrase\u00f1a", None))
        self.label_5.setText("")
        self.lineedit_verificar_contrasenia.setPlaceholderText(QCoreApplication.translate("DialogoCrearUsuario", u"  Confirmar Contrase\u00f1a", None))
        self.checkBox_estudiante.setText(QCoreApplication.translate("DialogoCrearUsuario", u"Estudiante ", None))
        self.checkBox_egresado.setText(QCoreApplication.translate("DialogoCrearUsuario", u"Egresado", None))
        self.checkBox_otro.setText(QCoreApplication.translate("DialogoCrearUsuario", u"Otro", None))
        self.label_7.setText("")
        self.lineedit_programa.setPlaceholderText(QCoreApplication.translate("DialogoCrearUsuario", u"  Programa", None))
    # retranslateUi

