# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogoAceptarReservaPqTeNx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import app.Vista.gui.imagenes_rc

class Ui_DialogAceptarReservas(object):
    def setupUi(self, DialogAceptarReservas):
        if not DialogAceptarReservas.objectName():
            DialogAceptarReservas.setObjectName(u"DialogAceptarReservas")
        DialogAceptarReservas.resize(333, 483)
        DialogAceptarReservas.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.buttonBox = QDialogButtonBox(DialogAceptarReservas)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 440, 311, 32))
        self.buttonBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonBox.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 0, 0);\n"
"	\n"
"	font: 14pt \"Tw Cen MT Condensed\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 208, 180);\n"
"	\n"
"	font: 14pt \"Tw Cen MT Condensed\";\n"
"\n"
"}")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.frame = QFrame(DialogAceptarReservas)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 333, 61))
        self.frame.setMinimumSize(QSize(333, 51))
        self.frame.setStyleSheet(u"background-color:  rgb(255, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 101, 41))
        self.label.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 20pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(182, 10, 141, 41))
        self.label_2.setStyleSheet(u"image: url(:/imagenes/imagenes/logo-udemedellin-footer.png);")
        self.label_2.setPixmap(QPixmap(u"../imagenes/logo-udemedellin-footer.png"))
        self.label_2.setScaledContents(True)
        self.scrollArea = QScrollArea(DialogAceptarReservas)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 60, 331, 371))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 312, 970))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 20pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_4.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 20pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.label_3.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 20pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.label_5.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_5.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 20pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.label_6.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_6.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_6)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 20pt \"Tw Cen MT Condensed\";\n"
"border: None;")
        self.label_7.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_7.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_7)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(DialogAceptarReservas)
        self.buttonBox.accepted.connect(DialogAceptarReservas.accept)
        self.buttonBox.rejected.connect(DialogAceptarReservas.reject)

        QMetaObject.connectSlotsByName(DialogAceptarReservas)
    # setupUi

    def retranslateUi(self, DialogAceptarReservas):
        DialogAceptarReservas.setWindowTitle(QCoreApplication.translate("DialogAceptarReservas", u"DialogoAceptarReserva", None))
        self.label.setText(QCoreApplication.translate("DialogAceptarReservas", u"<html><head/><body><p><span style=\" color:#ffffff;\">Reglamento</span></p></body></html>", None))
        self.label_2.setText("")
        self.label_4.setText(QCoreApplication.translate("DialogAceptarReservas", u"1. El uso del gimnasio es exclusivo para estudiantes, empleados y egresados de la Universidad de Medell\u00edn.", None))
        self.label_3.setText(QCoreApplication.translate("DialogAceptarReservas", u"2. El ingreso es \u00fanicamente presentando el carn\u00e9 que lo acredite como estudiante, empleado o egresado de la Universidad de Medell\u00edn.", None))
        self.label_5.setText(QCoreApplication.translate("DialogAceptarReservas", u"3. El usuario reserva su turno con 1 d\u00eda de anticipaci\u00f3n, o en su defecto el mismo d\u00eda, sujeto a disponibilidad de cupo.\n"
"En caso que el usuario no utilice el TURNO reservado, se har\u00e1 acreedor a suspensiones peri\u00f3dicas para el uso del espacio.", None))
        self.label_6.setText(QCoreApplication.translate("DialogAceptarReservas", u"4. Est\u00e1 totalmente prohibido el ingreso en estado de embriaguez y/o bajo efectos de sustancias psicoactivas.", None))
        self.label_7.setText(QCoreApplication.translate("DialogAceptarReservas", u"5. Por la seguridad de los usuarios, no se permite el ingreso de envases de vidrio.", None))
    # retranslateUi

