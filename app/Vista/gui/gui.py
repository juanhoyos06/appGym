from app.Mundo.mundo import *
from app.Mundo.errores import *
from app.Vista.gui.ui_DialogoAceptarReserva import Ui_DialogAceptarReservas
from app.Vista.gui.ui_DialogoCambiarContrasenia import Ui_DialogCambiarContrasenia
from app.Vista.gui.ui_DialogoCrearUsuario import Ui_DialogoCrearUsuario
from app.Vista.gui.ui_DialogoRecuperarContrasenia import Ui_DialogRecuperarContrasenia

from app.Vista.gui.ui_VentanaDeInicio import Ui_VentanaDeInicio
from PySide2.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox, QInputDialog
from PySide2 import QtGui, QtCore, QtWidgets

from app.Vista.gui.ui_VentanaNoticias import Ui_VentanaNoticias
from app.Vista.gui.ui_VentanaOpiniones import Ui_VentanaOpiniones
from app.Vista.gui.ui_VentanaReservas import Ui_VentanaReservas
from app.Vista.gui.ui_VentanaTurno import Ui_VentanaTurno
from app.Vista.gui.ui_VentanaUsuario import Ui_VentanaUsuario

from datetime import date
from datetime import timedelta
import calendar
from deep_translator import GoogleTranslator

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
        self.ui.pbutton_recuperarContrasenia.clicked.connect(self.abrir_dialogo_recuperar_contrasenia)
        self.ui.pbutton_crearCuenta.clicked.connect(self.abrir_dialogo_crear_cuenta)

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
                self.ventana = VentanaReservas(capturaUsuario, self.gym)
                self.ventana.show()

        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos obligatorios.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

    def abrir_dialogo_recuperar_contrasenia(self):
        dialog = DialogoRecuperarContrasenia(self)
        resp = dialog.exec_()

        if resp == QDialog.Accepted:
            capturaCedula = dialog.ui.lineedit_cedula.text()
            capturaContrasenia = dialog.ui.lineedit_contrasenia.text()
            capturaConfirmarContrasenia = dialog.ui.lineedit_recuperarContrasenia.text()

            if capturaCedula and capturaContrasenia  \
                and capturaConfirmarContrasenia:

                try:
                    self.gym.recuperar_contrasenia(capturaCedula,capturaContrasenia, capturaConfirmarContrasenia)

                except ContraseniasDiferentes as err:
                    msg_box = QMessageBox(self)
                    msg_box.setWindowTitle("Error recuperando contraseña.")
                    msg_box.setIcon(QMessageBox.Critical)
                    msg_box.setText(err.msg)
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    msg_box.exec_()

                except UsuarioNoExistenteError as err:
                    msg_box = QMessageBox(self)
                    msg_box.setWindowTitle("Error recuperando contraseña.")
                    msg_box.setIcon(QMessageBox.Critical)
                    msg_box.setText(err.msg)
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    msg_box.exec_()
                else:
                    msg_box = QMessageBox(self)
                    msg_box.setWindowTitle("Operacion Exitosa")
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setText("Contraseña recuperada exitosamente correctamente.")
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    msg_box.exec_()

            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error recuperando contraseña")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText("Debe de ingresar todos los campos")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

    def abrir_dialogo_crear_cuenta(self):
        dialog = DialogoCrearUsuario(self)
        resp = dialog.exec_()

        if resp == QDialog.Accepted:
            cedula = dialog.ui.lineedit_cedula_3.text()
            nombre = dialog.ui.lineedit_nombre.text()
            telefono = dialog.ui.lineedit_telefono.text()
            correo = dialog.ui.lineedit_correo.text()
            edad = dialog.ui.lineedit_edad.text()
            genero = dialog.ui.comboBox_genero.currentText()
            programa = dialog.ui.comboBox_facultades.currentText()
            contrasenia = dialog.ui.lineedit_contrasenia.text()
            confirmarContrasenia = dialog.ui.lineedit_verificar_contrasenia.text()
            cargo = ""
            if dialog.ui.checkBox_estudiante.isChecked():
                cargo = "Estudiante"

            elif dialog.ui.checkBox_egresado.isChecked():
                cargo = "Egresado"

            elif dialog.ui.checkBox_otro.isChecked():
                cargo = "Otro"



            try:
                self.gym.crear_usuario(cedula, nombre.upper(), telefono , correo.upper(), edad, genero, contrasenia, confirmarContrasenia, cargo.upper())

            except ContraseniasDiferentes as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error creando usuario.")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

            except CorreoInvalido as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error creando usuario.")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

            except ErrorMultiple as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error creando usuario.")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

            except UsuarioExistenteError as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error creando usuario.")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Operacion Exitosa")
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Usuario creado exitosamente")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
                if programa != "NO APLICA":
                    dialog.gym.relacionar_usuario_programa(cedula, programa)

class VentanaReservas(QMainWindow):
    def __init__(self, cedula, gym: Gym):
        super().__init__()
        self.ventanaReservas = Ui_VentanaReservas()
        self.ventanaReservas.setupUi(self)
        self.gym = gym
        self.cedula = cedula
        self._configurar()



    def _configurar(self):
        """
        Metodo para la conexion de botones y labels con los metodos logicos

        :return:
        """
        traductor = GoogleTranslator(source='en', target='es') # instancia un objeto de la clase GoogleTranslator
        diaActual = date.today() #obtiene el dia actual en numero
        diaSiguiente = diaActual +  timedelta(days=1) #obtiene el dia Siguiente en numero, sumandole uno al dia actual
        nombreDia = traductor.translate(calendar.day_name[diaActual.weekday()]) #nombre del dia actual
        nombreDiaSiguiente = traductor.translate(calendar.day_name[diaSiguiente.weekday()])#nombre del dia siguiente
        mesActual = traductor.translate(calendar.month_name[diaActual.month]) #nombre del mes  del dia actual
        mesSiguiente = traductor.translate(calendar.month_name[diaSiguiente.month]) #nombre del mes del dia siguiente

        if nombreDia == "Sábado" or nombreDia == "Domingo": #Comprueba si los dias son diferentes al fin de semana
            self.ventanaReservas.pbutton_reservadia.setEnabled(False)#Deshabilita los botones
        if nombreDiaSiguiente == "Sábado" or nombreDiaSiguiente == "Domingo": #Comprueba si los dias son diferentes al fin de semana
            self.ventanaReservas.pbutton_reservadiaSig.setEnabled(False) #Deshabilita los botones

        self.ventanaReservas.label_diaActual.setText(nombreDia) # Lleva el nombre del dia al label
        self.ventanaReservas.label_fechaActual.setText(str(diaActual.day)) # lleva el numero del dia al label

        self.ventanaReservas.label_mesActual.setText(str(mesActual)) # Lleva el nombre del mes al label
        self.ventanaReservas.label_diaSiguiente.setText(nombreDiaSiguiente)# Lleva el nombre del dia siguiente al label
        self.ventanaReservas.label_fechaSiguiente.setText(str(diaSiguiente.day)) # lleva el numero del dia siguiente al label

        self.ventanaReservas.pbutton_cerrar_sesion.clicked.connect(self.cerrar_sesion)

        self.ventanaReservas.label_mesSiguiente.setText(str(mesSiguiente))#Lleva el nombre del mes siguiente al label


        fechaActual = datetime.strftime(datetime.now(),"%d-%m-%y") #obtiene la fecha actual en el formato de sql
        reserva = self.gym.reservas_usuario_dia_actual(self.cedula,fechaActual) #obtiene las reservas del usuario
                                                            # junto con la hora de la reserva


        if reserva != []:       #Verifica si el usuario tiene reserva
            self.ventanaReservas.label_recuerdoDiaActual.setText(f"Recuerde su reservas a las\n {reserva[0][1]}")
                    #Si el usuario tiene reserva lleva un mensaje de recordatorio con la hora de la reserva al label

        fechaSig = datetime.strftime(datetime.now()+ timedelta(days=1),"%d-%m-%y")#obtiene la fecha siguiente en el formato de sql
        reservaSig = self.gym.reservas_usuario_dia_actual(self.cedula,fechaSig) #obtiene las reservas del usuario
                                                            # junto con la hora de la reserva
        if reservaSig != []:         #Verifica si el usuario tiene reserva
            self.ventanaReservas.label_recuerdoDiaSiguiente.setText(f"Recuerde su reservas a las\n {reservaSig[0][1]}")
                    # Si el usuario tiene reserva lleva un mensaje de recordatorio con la hora de la reserva al label

        cuposDiaActual = self.gym.cupos_disponibles_por_dia(fechaActual) # Guarda los cupos disponibles para el dia actual
        if cuposDiaActual > 0:      #Evalua si aun hay cupos y  siendo asi pone los numeros del dia en verde
            self.ventanaReservas.label_fechaActual.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
                                                                 "font: 30pt \"Tw Cen MT Condensed\";\n"
                                                                 "border: None;" "\n color:#57b400;")  # Pone el color al numero
        else:       #Sino hay cupos pone los numeros del dia en rojo
            self.ventanaReservas.label_fechaActual.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
                                                                 "font: 30pt \"Tw Cen MT Condensed\";\n"
                                                                 "border: None;" "\n color:#f90808;")  # Pone el color al numero

        cuposDiaSig = self.gym.cupos_disponibles_por_dia(fechaSig) # Guarda los cupos disponibles para el dia siguiente
        if cuposDiaSig >0:      #Evalua si aun hay cupos y  siendo asi pone los numeros del dia en verde
            self.ventanaReservas.label_fechaSiguiente.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
                                                                    "font: 30pt \"Tw Cen MT Condensed\";\n"
                                                                    "border: None;" "\n  color:#57b400;")  # Pone el color al numero
        else:       #Sino hay cupos pone los numeros del dia en rojo
            self.ventanaReservas.label_fechaSiguiente.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
                                                                    "font: 30pt \"Tw Cen MT Condensed\";\n"
                                                                    "border: None;" "\n  color:#f90808;")  # Pone el color al numero


        self.ventanaReservas.pbutton_reservadia.clicked.connect(self.abrir_turnos_actual)#Conecta los botones para reservas con los turnos
        self.ventanaReservas.pbutton_reservadiaSig.clicked.connect(self.abrir_turnos_sig)#Conecta los botones para reservas con los turnos
        self.ventanaReservas.tbutton_opinion.clicked.connect(self.abrir_opinion)#Conecta los botones del menu inferior con las ventanas
        self.ventanaReservas.tbutton_noticias.clicked.connect(self.abrir_noticias)#Conecta los botones del menu inferior con las ventanas
        self.ventanaReservas.tbutton_usuario.clicked.connect(self.abrir_usuario)#Conecta los botones del menu inferior con las ventanas


    def abrir_turnos_actual(self):
        """
        Metodo que abre la ventana de los turnos del dia actual
        :return:
        """
        fechaActual = datetime.strftime(datetime.now(), "%d-%m-%y")
        self.hide()
        self.ventana = VentanaTurnos(self.cedula, self.gym, fechaActual)
        self.ventana.show()

    def abrir_turnos_sig(self):
        """
        Metodo que abre la ventana de los turnos del dia siguiente
        :return:
        """
        fechaSig = datetime.strftime(datetime.now() + timedelta(days=1), "%d-%m-%y")
        self.hide()
        self.ventana = VentanaTurnos(self.cedula, self.gym, fechaSig)
        self.ventana.show()

    def abrir_opinion(self):
        """
        Metodo que abre la ventana de opiniones
        :return:
        """
        self.hide()
        self.ventanaO = VentanaOpiniones(self.cedula, self.gym)
        self.ventanaO.show()

    def cerrar_sesion(self):
        """
        Metodo que cierra sesion y abre la ventana de login
        :return:
        """
        self.hide()
        self.ventanaO = VentanaLogin(self.gym)
        self.ventanaO.show()

    def abrir_noticias(self):
        """
        Metodo que abre la ventana de noticias
        :return:
        """
        self.hide()
        self.ventanaN = VentanaNoticias(self.cedula, self.gym)
        self.ventanaN.show()

    def abrir_usuario(self):
        """
        Metodo que abre la ventana de usuario
        :return:
        """
        self.hide()
        self.ventanaU = VentanaUsuario(self.cedula, self.gym)
        self.ventanaU.show()

class VentanaTurnos(QMainWindow):
    def __init__(self, cedula, gym : Gym, fecha):
        super().__init__()
        self.ventanaTurno = Ui_VentanaTurno()
        self.ventanaTurno.setupUi(self)
        self.gym = gym
        self.fecha = fecha
        self.cedula = cedula
        self.ventanaTurno.tbutton_opinion.clicked.connect(self.abrir_opinion)
        self.ventanaTurno.tbutton_noticias.clicked.connect(self.abrir_noticias)
        self.ventanaTurno.tbutton_usuario.clicked.connect(self.abrir_usuario)
        self.ventanaTurno.tbutton_reserva.clicked.connect(self.abrir_reserva)

        self.ventanaTurno.pbutton_turno1.clicked.connect(self.abrir_dialogo_aceptar_reserva_turno1)
        self.ventanaTurno.pbutton_turno2.clicked.connect(self.abrir_dialogo_aceptar_reserva_turno2)
        self.ventanaTurno.pbutton_turno3.clicked.connect(self.abrir_dialogo_aceptar_reserva_turno3)
        self.ventanaTurno.pbutton_turno4.clicked.connect(self.abrir_dialogo_aceptar_reserva_turno4)
        self.ventanaTurno.pbutton_turno5.clicked.connect(self.abrir_dialogo_aceptar_reserva_turno5)
        self.ventanaTurno.pbutton_turno6.clicked.connect(self.abrir_dialogo_aceptar_reserva_turno6)
        self.ventanaTurno.pbutton_turno7.clicked.connect(self.abrir_dialogo_aceptar_reserva_turno7)
        self.ventanaTurno.pbutton_eliminarReserva.clicked.connect(self.eliminar_reserva)
        self.ventanaTurno.pbutton_cerrar_sesion.clicked.connect(self.cerrar_sesion)

        self._configurar()

    def _configurar(self):
        cuposDisponiblesT1 = self.gym.cupos_disponibles_por_turno(self.fecha,'6:00')
        cuposDisponiblesT2 = self.gym.cupos_disponibles_por_turno(self.fecha,'8:00')
        cuposDisponiblesT3 = self.gym.cupos_disponibles_por_turno(self.fecha,'10:00')
        cuposDisponiblesT4 = self.gym.cupos_disponibles_por_turno(self.fecha,'12:00')
        cuposDisponiblesT5 = self.gym.cupos_disponibles_por_turno(self.fecha,'14:00')
        cuposDisponiblesT6 = self.gym.cupos_disponibles_por_turno(self.fecha,'16:00')
        cuposDisponiblesT7 = self.gym.cupos_disponibles_por_turno(self.fecha,'18:00')
        fecha_t1 = datetime.strptime("6:00:00", "%H:%M:%S").time()
        fecha_t2 = datetime.strptime("8:00:00", "%H:%M:%S").time()
        fecha_t3 = datetime.strptime("10:00:00", "%H:%M:%S").time()
        fecha_t4 = datetime.strptime("12:00:00", "%H:%M:%S").time()
        fecha_t5 = datetime.strptime("14:00:00", "%H:%M:%S").time()
        fecha_t6 = datetime.strptime("16:00:00", "%H:%M:%S").time()
        fecha_t7 = datetime.strptime("18:00:00", "%H:%M:%S").time()
        fechaActual = datetime.strftime(datetime.now(),"%d-%m-%y")



        if cuposDisponiblesT1 == 0 or ( self.fecha == fechaActual and datetime.now().time() > fecha_t1):
            self.ventanaTurno.pbutton_turno1.setEnabled(False)

        if cuposDisponiblesT2 == 0 or ( self.fecha == fechaActual and datetime.now().time() > fecha_t2):
            self.ventanaTurno.pbutton_turno2.setEnabled(False)

        if cuposDisponiblesT3 == 0 or ( self.fecha == fechaActual and datetime.now().time() > fecha_t3):
            self.ventanaTurno.pbutton_turno3.setEnabled(False)

        if cuposDisponiblesT4 == 0 or ( self.fecha == fechaActual and datetime.now().time() > fecha_t4):
            self.ventanaTurno.pbutton_turno4.setEnabled(False)

        if cuposDisponiblesT5 == 0 or ( self.fecha == fechaActual and datetime.now().time() > fecha_t5):
            self.ventanaTurno.pbutton_turno5.setEnabled(False)

        if cuposDisponiblesT6 == 0 or ( self.fecha == fechaActual and datetime.now().time() > fecha_t6):
            self.ventanaTurno.pbutton_turno6.setEnabled(False)

        if cuposDisponiblesT7 == 0 or ( self.fecha == fechaActual and datetime.now().time() > fecha_t7):
            self.ventanaTurno.pbutton_turno7.setEnabled(False)



        self.ventanaTurno.pbutton_turno1.setText(f"6:00AM - 8:00AM                      {cuposDisponiblesT1} Cupos Disponibles")
        self.ventanaTurno.pbutton_turno2.setText(f"8:00AM - 10:00AM                     {cuposDisponiblesT2} Cupos Disponibles")
        self.ventanaTurno.pbutton_turno3.setText(f"10:00AM - 12:00AM                    {cuposDisponiblesT3} Cupos Disponibles")
        self.ventanaTurno.pbutton_turno4.setText(f"12:00AM - 2:00PM                      {cuposDisponiblesT4} Cupos Disponibles")
        self.ventanaTurno.pbutton_turno5.setText(f"2:00PM - 4:00PM                      {cuposDisponiblesT5} Cupos Disponibles")
        self.ventanaTurno.pbutton_turno6.setText(f"4:00PM - 6:00PM                      {cuposDisponiblesT6} Cupos Disponibles")
        self.ventanaTurno.pbutton_turno7.setText(f"6:00PM - 8:00PM                      {cuposDisponiblesT7} Cupos Disponibles")

    def cerrar_sesion(self):
        """
        Metodo que cierra sesion y abre la ventana de login
        :return:
        """
        self.hide()
        self.ventanaO = VentanaLogin(self.gym)
        self.ventanaO.show()

    def abrir_dialogo_aceptar_reserva_turno1(self):
        dialog = DialogoAceptarReserva(self)
        resp = dialog.exec_()
        hora = "6:00"
        if resp  == QDialog.Accepted:
            try:
                self.gym.realizar_reserva(self.cedula, self.fecha, hora)
            except ReservaExistenteError as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error realizando reserva ")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Operacion Exitosa")
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Reserva realizada correctamente.")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
                self._configurar()

    def abrir_dialogo_aceptar_reserva_turno2(self):
        dialog = DialogoAceptarReserva(self)
        resp = dialog.exec_()
        hora = "8:00"
        if resp  == QDialog.Accepted:
            try:
                self.gym.realizar_reserva(self.cedula, self.fecha, hora)
            except ReservaExistenteError as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error realizando reserva ")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Operacion Exitosa")
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Reserva realizada correctamente.")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
                self._configurar()

    def abrir_dialogo_aceptar_reserva_turno3(self):
        dialog = DialogoAceptarReserva(self)
        resp = dialog.exec_()
        hora = "10:00"
        if resp  == QDialog.Accepted:
            try:
                self.gym.realizar_reserva(self.cedula, self.fecha, hora)
            except ReservaExistenteError as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error realizando reserva ")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Operacion Exitosa")
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Reserva realizada correctamente.")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
                self._configurar()

    def abrir_dialogo_aceptar_reserva_turno4(self):
        dialog = DialogoAceptarReserva(self)
        resp = dialog.exec_()
        hora = "12:00"
        if resp  == QDialog.Accepted:
            try:
                self.gym.realizar_reserva(self.cedula, self.fecha, hora)
            except ReservaExistenteError as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error realizando reserva ")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Operacion Exitosa")
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Reserva realizada correctamente.")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
                self._configurar()

    def abrir_dialogo_aceptar_reserva_turno5(self):
        dialog = DialogoAceptarReserva(self)
        resp = dialog.exec_()
        hora = "14:00"
        if resp  == QDialog.Accepted:
            try:
                self.gym.realizar_reserva(self.cedula, self.fecha, hora)
            except ReservaExistenteError as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error realizando reserva ")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Operacion Exitosa")
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Reserva realizada correctamente.")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
                self._configurar()

    def abrir_dialogo_aceptar_reserva_turno6(self):
        dialog = DialogoAceptarReserva(self)
        resp = dialog.exec_()
        hora = "16:00"
        if resp  == QDialog.Accepted:
            try:
                self.gym.realizar_reserva(self.cedula, self.fecha, hora)
            except ReservaExistenteError as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error realizando reserva ")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Operacion Exitosa")
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Reserva realizada correctamente.")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
                self._configurar()

    def abrir_dialogo_aceptar_reserva_turno7(self):
        dialog = DialogoAceptarReserva(self)
        resp = dialog.exec_()
        hora = "18:00"
        if resp  == QDialog.Accepted:
            try:
                self.gym.realizar_reserva(self.cedula, self.fecha, hora)
            except ReservaExistenteError as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error realizando reserva ")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Operacion Exitosa")
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Reserva realizada correctamente.")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
                self._configurar()

    def abrir_reserva(self):
        self.hide()
        self.ventana = VentanaReservas(self.cedula, self.gym)
        self.ventana.show()

    def abrir_opinion(self):
        self.hide()
        self.ventanaO = VentanaOpiniones(self.cedula, self.gym)
        self.ventanaO.show()

    def abrir_noticias(self):
        self.hide()
        self.ventana = VentanaNoticias(self.cedula, self.gym)
        self.ventana.show()

    def abrir_usuario(self):
        self.hide()
        self.ventana = VentanaUsuario(self.cedula, self.gym)
        self.ventana.show()

    def eliminar_reserva(self):

        try:
            self.gym.eliminar_reserva(self.cedula, self.fecha)
        except ReservaNoExistenteError as err:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error eliminando reserva.")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText(err.msg)
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Operacion Exitosa")
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Reserva eliminada exitosamente")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

            self._configurar()

class VentanaOpiniones(QMainWindow):
    def __init__(self, cedula, gym : Gym):
        super().__init__()
        self.ventanaOpiniones = Ui_VentanaOpiniones()
        self.ventanaOpiniones.setupUi(self)
        self.cedula = cedula
        self.gym = gym
        self.ventanaOpiniones.tbutton_reserva.clicked.connect(self.abrir_reserva)
        self.ventanaOpiniones.tbutton_noticias.clicked.connect(self.abrir_noticias)
        self.ventanaOpiniones.tbutton_usuario.clicked.connect(self.abrir_usuario)
        self.ventanaOpiniones.pushButton.clicked.connect(self.enviar_opinion)
        self.ventanaOpiniones.pbutton_cerrar_sesion.clicked.connect(self.cerrar_sesion)

    def cerrar_sesion(self):
        """
        Metodo que cierra sesion y abre la ventana de login
        :return:
        """
        self.hide()
        self.ventanaO = VentanaLogin(self.gym)
        self.ventanaO.show()


    def abrir_reserva(self):
        self.hide()
        self.ventana = VentanaReservas(self.cedula,self.gym)
        self.ventana.show()

    def abrir_noticias(self):
        self.hide()
        self.ventana = VentanaNoticias(self.cedula, self.gym)
        self.ventana.show()

    def abrir_usuario(self):
        self.hide()
        self.ventana = VentanaUsuario(self.cedula, self.gym)
        self.ventana.show()

    def enviar_opinion(self):

        fechaActual = datetime.strftime(datetime.now(), "%d-%m-%y")
        descripcion = self.ventanaOpiniones.textedit_descripcion.toPlainText()
        asunto = self.ventanaOpiniones.lineedit_asunto.text()

        if descripcion and asunto:

            self.gym.enviar_opinion(self.cedula, descripcion, fechaActual, asunto)

            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Operacion Exitosa")
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Opinion enviada correctamente")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

            self.ventanaOpiniones.textedit_descripcion.clear()
            self.ventanaOpiniones.lineedit_asunto.clear()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos obligatorios.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

class VentanaUsuario(QMainWindow):
    def __init__(self, cedula, gym: Gym):
        super().__init__()
        self.ventanaUsuario = Ui_VentanaUsuario()
        self.ventanaUsuario.setupUi(self)
        self.cedula = cedula
        self.gym = gym
        self.ventanaUsuario.tbutton_opinion.clicked.connect(self.abrir_opinion)
        self.ventanaUsuario.tbutton_noticias.clicked.connect(self.abrir_noticias)
        self.ventanaUsuario.tbutton_reserva.clicked.connect(self.abrir_reserva)
        self.ventanaUsuario.pbutton_cerrar_sesion.clicked.connect(self.cerrar_sesion)
        self.ventanaUsuario.pbutton_cambiar_contrasenia.clicked.connect(self.abrir_dialogo_cambiar_contrasenia)
        self._configurar()

    def _configurar(self):
        datos = self.gym.obtener_datos_usuario(self.cedula)
        self.ventanaUsuario.label_nombre.setText(str(datos[0][0]))
        self.ventanaUsuario.label_telefono.setText(str(datos[0][3]))
        self.ventanaUsuario.label_correo.setText(str(datos[0][4]))
        self.ventanaUsuario.label_edad.setText(str(datos[0][1]))
        if str(datos[0][2]) == "Otro":
            datos[0][2] = "Indefinido"
        self.ventanaUsuario.label_sexo.setText(str(datos[0][2]))



    def abrir_dialogo_cambiar_contrasenia(self):
        dialog = DialogoCambiarContrasenia(self)
        resp = dialog.exec_()

        if resp == QDialog.Accepted:
            capturaCedula = dialog.ui.lineedit_cedula.text()
            capturaContrasenia = dialog.ui.lineedit_contrasenia.text()
            capturaConfirmarContrasenia = dialog.ui.lineedit_recuperarContrasenia.text()

            if capturaCedula and capturaContrasenia  \
                and capturaConfirmarContrasenia:

                try:
                    self.gym.recuperar_contrasenia(capturaCedula,capturaContrasenia, capturaConfirmarContrasenia)

                except ContraseniasDiferentes as err:
                    msg_box = QMessageBox(self)
                    msg_box.setWindowTitle("Error recuperando contraseña.")
                    msg_box.setIcon(QMessageBox.Critical)
                    msg_box.setText(err.msg)
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    msg_box.exec_()



                except UsuarioNoExistenteError as err:
                    msg_box = QMessageBox(self)
                    msg_box.setWindowTitle("Error recuperando contraseña.")
                    msg_box.setIcon(QMessageBox.Critical)
                    msg_box.setText(err.msg)
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    msg_box.exec_()

                else:
                    msg_box = QMessageBox(self)
                    msg_box.setWindowTitle("Operacion Exitosa")
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setText("Contraseña recuperada exitosamente correctamente.")
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    msg_box.exec_()

            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error recuperando contraseña")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText("Debe de ingresar todos los campos")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()


    def cerrar_sesion(self):
        """
        Metodo que cierra sesion y abre la ventana de login
        :return:
        """
        self.hide()
        self.ventanaO = VentanaLogin(self.gym)
        self.ventanaO.show()

    def abrir_reserva(self):
        self.hide()
        self.ventana = VentanaReservas(self.cedula, self.gym)
        self.ventana.show()

    def abrir_noticias(self):
        self.hide()
        self.ventana = VentanaNoticias(self.cedula, self.gym)
        self.ventana.show()

    def abrir_opinion(self):
        self.hide()
        self.ventana = VentanaOpiniones(self.cedula, self.gym)
        self.ventana.show()

class VentanaNoticias(QMainWindow):
    def __init__(self, cedula, gym:Gym):
        super().__init__()
        self.ventanaNoticias = Ui_VentanaNoticias()
        self.ventanaNoticias.setupUi(self)
        self.cedula = cedula
        self.gym = gym
        self.ventanaNoticias.tbutton_opinion.clicked.connect(self.abrir_opinion)
        self.ventanaNoticias.tbutton_usuario.clicked.connect(self.abrir_usuario)
        self.ventanaNoticias.tbutton_reservas.clicked.connect(self.abrir_reserva)
        self.ventanaNoticias.pbutton_cerrar_sesion.clicked.connect(self.cerrar_sesion)

    def cerrar_sesion(self):
        """
        Metodo que cierra sesion y abre la ventana de login
        :return:
        """
        self.hide()
        self.ventanaO = VentanaLogin(self.gym)
        self.ventanaO.show()

    def abrir_reserva(self):
        self.hide()
        self.ventana = VentanaReservas(self.cedula,self.gym)
        self.ventana.show()

    def abrir_usuario(self):
        self.hide()
        self.ventana = VentanaUsuario(self.cedula,self.gym)
        self.ventana.show()

    def abrir_opinion(self):
        self.hide()
        self.ventana = VentanaOpiniones(self.cedula,self.gym)
        self.ventana.show()

class DialogoAceptarReserva(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        self.ui = Ui_DialogAceptarReservas()
        self.ui.setupUi(self)


    def accept(self) -> None:
        super().accept()

class DialogoRecuperarContrasenia(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        self.ui = Ui_DialogRecuperarContrasenia()
        self.ui.setupUi(self)


    def accept(self) -> None:
        super().accept()

class DialogoCrearUsuario(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        self.ui = Ui_DialogoCrearUsuario()
        self.gym = Gym()
        self.ui.setupUi(self)
        self.generos = ["Seleccionar", "Masculino", "Femenino", "Otro"]
        self.ui.comboBox_genero.addItems(self.generos)
        self.facultades = ["NO APLICA"]
        facultades = self.gym.seleccionar_facultad()
        for i in facultades:
            self.facultades.append(str(i[0]))

        self.ui.comboBox_facultades.addItems(self.facultades)




    def accept(self) -> None:
        cedula = self.ui.lineedit_cedula_3.text()
        nombre = self.ui.lineedit_nombre.text()
        telefono = self.ui.lineedit_telefono.text()
        correo = self.ui.lineedit_correo.text()
        edad = self.ui.lineedit_edad.text()
        genero = self.ui.comboBox_genero.currentText()
        contrasenia = self.ui.lineedit_contrasenia.text()
        confirmarContrasenia = self.ui.lineedit_verificar_contrasenia.text()
        cargo = ""
        if self.ui.checkBox_estudiante.isChecked():
            cargo = "Estudiante"

        elif self.ui.checkBox_egresado.isChecked():
            cargo = "Egresado"

        elif self.ui.checkBox_otro.isChecked():
            cargo = "Otro"

        if (cedula and nombre and telefono and correo and edad and genero != "Seleccionar"
                and contrasenia and confirmarContrasenia and cargo):
            super().accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error creando cuenta ")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe de ingresar todos los campos")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

class DialogoCambiarContrasenia(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        self.ui = Ui_DialogCambiarContrasenia()
        self.ui.setupUi(self)



    def accept(self) -> None:
        super().accept()
