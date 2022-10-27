from app.Mundo.mundo import *
from app.Mundo.errores import *
from app.Vista.gui.ui_VentanaDeInicio import Ui_VentanaDeInicio
from PySide2.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox, QInputDialog
from PySide2 import QtGui, QtCore, QtWidgets

from app.Vista.gui.ui_VentanaNoticias import Ui_VentanaNoticias
from app.Vista.gui.ui_VentanaOpiniones import Ui_VentanaOpiniones
from app.Vista.gui.ui_VentanaReservas import Ui_VentanaReservas
from app.Vista.gui.ui_VentanaTurno import Ui_VentanaTurno
from app.Vista.gui.ui_VentanaUsuario import Ui_VentanaUsuario


class VentanaLogin(QMainWindow):
    def __init__(self, gym : Gym):
        QMainWindow.__init__(self)
        self.gym = gym
        self.ui = Ui_VentanaDeInicio()
        self.ui.setupUi(self)
        self.c = Conexion()
        self._configurar()
        self.show()

    def _configurar(self):
        """
        Metodo para la conexion de botones con los metodos logicos

        :return:
        """
        self.ui.pbutton_ingresar.clicked.connect(self.iniciar_sesion)

    def iniciar_sesion(self):
        capturaUsuario = self.ui.lineedit_usuario.text()
        capturaContrasenia = self.ui.lineedit_contrasenia.text()

        if capturaUsuario != "" and capturaContrasenia != "":
            try:
                self.gym.iniciar_sesion(capturaUsuario, capturaContrasenia)
            except Usuario_o_ContraseniaIncorrecto as e:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error iniciando sesion")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(e.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                self.hide()
                self.ventana = VentanaReservas(capturaUsuario)
                self.ventana.show()

        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setStyleSheet('background-color: None')
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos obligatorios.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()




class VentanaReservas(QMainWindow):
    def __init__(self, cedula):
        super().__init__()
        self.ventanaReservas = Ui_VentanaReservas()
        self.ventanaReservas.setupUi(self)
        self._configurar()
        self.cedula = cedula


    def _configurar(self):
        """
        Metodo para la conexion de botones con los metodos logicos

        :return:
        """

        self.ventanaReservas.pbutton_reservadia.clicked.connect(self.abrir_turnos)
        self.ventanaReservas.pbutton_reservadiaSig.clicked.connect(self.abrir_turnos)
        self.ventanaReservas.tbutton_opinion.clicked.connect(self.abrir_opinion)
        self.ventanaReservas.tbutton_noticias.clicked.connect(self.abrir_noticias)
        self.ventanaReservas.tbutton_usuario.clicked.connect(self.abrir_usuario)


    def abrir_turnos(self):
        self.hide()
        self.ventana = VentanaTurnos(self.cedula)
        self.ventana.show()

    def abrir_opinion(self):
        self.hide()
        self.ventanaO = VentanaOpiniones(self.cedula)
        self.ventanaO.show()

    def abrir_noticias(self):
        self.hide()
        self.ventana = VentanaNoticias(self.cedula)
        self.ventana.show()

    def abrir_usuario(self):
        self.hide()
        self.ventana = VentanaUsuario(self.cedula)
        self.ventana.show()

class VentanaTurnos(QMainWindow):
    def __init__(self, cedula):
        super().__init__()
        self.ventanaTurno = Ui_VentanaTurno()
        self.ventanaTurno.setupUi(self)
        self._configurar()
        self.cedula = cedula
        self.ventanaTurno.tbutton_opinion.clicked.connect(self.abrir_opinion)
        self.ventanaTurno.tbutton_noticias.clicked.connect(self.abrir_noticias)
        self.ventanaTurno.tbutton_usuario.clicked.connect(self.abrir_usuario)
        self.ventanaTurno.tbutton_reserva.clicked.connect(self.abrir_reserva)

    def abrir_reserva(self):
        self.hide()
        self.ventana = VentanaReservas(self.cedula)
        self.ventana.show()

    def abrir_opinion(self):
        self.hide()
        self.ventanaO = VentanaOpiniones(self.cedula)
        self.ventanaO.show()

    def abrir_noticias(self):
        self.hide()
        self.ventana = VentanaNoticias(self.cedula)
        self.ventana.show()

    def abrir_usuario(self):
        self.hide()
        self.ventana = VentanaUsuario(self.cedula)
        self.ventana.show()

    def _configurar(self):
        pass

class VentanaOpiniones(QMainWindow):
    def __init__(self, cedula):
        super().__init__()
        self.ventanaOpiniones = Ui_VentanaOpiniones()
        self.ventanaOpiniones.setupUi(self)
        self.cedula = cedula
        self.ventanaOpiniones.tbutton_reserva.clicked.connect(self.abrir_reserva)
        self.ventanaOpiniones.tbutton_noticias.clicked.connect(self.abrir_noticias)
        self.ventanaOpiniones.tbutton_usuario.clicked.connect(self.abrir_usuario)


    def abrir_reserva(self):
        self.hide()
        self.ventana = VentanaReservas(self.cedula)
        self.ventana.show()

    def abrir_noticias(self):
        self.hide()
        self.ventana = VentanaNoticias(self.cedula)
        self.ventana.show()

    def abrir_usuario(self):
        self.hide()
        self.ventana = VentanaUsuario(self.cedula)
        self.ventana.show()

class VentanaUsuario(QMainWindow):
    def __init__(self, cedula):
        super().__init__()
        self.ventanaUsuario = Ui_VentanaUsuario()
        self.ventanaUsuario.setupUi(self)
        self.cedula = cedula
        self.ventanaUsuario.tbutton_opinion.clicked.connect(self.abrir_opinion)
        self.ventanaUsuario.tbutton_noticias.clicked.connect(self.abrir_noticias)
        self.ventanaUsuario.tbutton_reserva.clicked.connect(self.abrir_reserva)

    def abrir_reserva(self):
        self.hide()
        self.ventana = VentanaReservas(self.cedula)
        self.ventana.show()

    def abrir_noticias(self):
        self.hide()
        self.ventana = VentanaNoticias(self.cedula)
        self.ventana.show()

    def abrir_opinion(self):
        self.hide()
        self.ventana = VentanaOpiniones(self.cedula)
        self.ventana.show()


class VentanaNoticias(QMainWindow):
    def __init__(self, cedula):
        super().__init__()
        self.ventanaNoticias = Ui_VentanaNoticias()
        self.ventanaNoticias.setupUi(self)
        self.cedula = cedula
        self.ventanaNoticias.tbutton_opinion.clicked.connect(self.abrir_opinion)
        self.ventanaNoticias.tbutton_usuario.clicked.connect(self.abrir_usuario)
        self.ventanaNoticias.tbutton_reservas.clicked.connect(self.abrir_reserva)

    def abrir_reserva(self):
        self.hide()
        self.ventana = VentanaReservas(self.cedula)
        self.ventana.show()

    def abrir_usuario(self):
        self.hide()
        self.ventana = VentanaUsuario(self.cedula)
        self.ventana.show()

    def abrir_opinion(self):
        self.hide()
        self.ventana = VentanaOpiniones(self.cedula)
        self.ventana.show()

