from app.Mundo.conexion import Conexion
from app.Mundo.errores import *
from datetime import date
from datetime import datetime

class Reserva:

    def __init__ (self, fecha, hora, nombre_usuario):
        self.fecha = fecha
        self.hora = hora
        self.nombre_usuario: str = nombre_usuario


class Opinion:

    def __init__(self, nombre_usuario, descripcion):
        self.nombre_usuario: str = nombre_usuario
        self.descripcion: str = descripcion

class Usuario:

    def __init__(self, cedula, nombre, edad, sexo, correo, telefono, contrasenia, cargo):
        self.cedula: int = cedula
        self.nombre: str = nombre
        self.edad: int = edad
        self.sexo: str = sexo
        self.correo: str = correo
        self.telefono: int = telefono
        self.contrasenia: str = contrasenia
        self.cargo: str = cargo
        self.c = Conexion()
class Gym:

    def __init__(self):
        self.c = Conexion()

    def buscar_usuario(self, cedula):
        """
        Se encarga de buscar si un usuario esta dentro de la base de datos

        :param cedula: Identificador del usuario
        :return: El identificador del usuario en una lista si el usuario existe, si no, la lista estara vacia
        """

        consulta = f"SELECT id_usuario FROM Usuario WHERE id_usuario = '{cedula}'"
        return self.c.select_in_database(consulta)

    def crear_usuario(self,cedula, nombre, telefono , correo, edad, sexo,  contrasenia, verificarContrasenia, cargo):
        """
        Se encarga de evaluar si un usuario esta o no dentro de la base de datos, si esta muestra un mensaje
        de error, sino, lo agrega


        :param cedula: identificador del usuario
        :param nombre: nombre del usuario
        :param edad: edad del usuario
        :param correo: correo electronico del usuario
        :param telefono: telefono del usuario
        :param contrasenia: contraseña del usuario

        """

        consultaInsert = f"INSERT INTO Usuario VALUES('{cedula}', '{nombre}','{edad}'," \
                         f"'{sexo}','{telefono}','{correo}','{contrasenia}', '{cargo}') "


        if self.buscar_usuario(cedula) == [] and contrasenia == verificarContrasenia:
            self.c.insert_in_database(consultaInsert)
        elif self.buscar_usuario(cedula) == [] and contrasenia != verificarContrasenia:
            raise ContraseniasDiferentes("Las contraseñas no coinciden")

        else:
            raise UsuarioExistenteError(cedula, f"Ya existe un usuario con la cedula{cedula}")

    def buscar_contrasenia(self, cedula):
        """
        Se encarga de buscar la contraseña del usuario
        :param cedula: Identificador del usuario
        :return: La contraseña del usuario en una lista si el usuario existe, si no, la lista estara vacia
        """
        consulta = f"SELECT contraseña FROM Usuario WHERE id_usuario = '{cedula}'"
        return self.c.select_in_database(consulta)

    def iniciar_sesion(self, cedula_usuario, contraseniaUsuario):
        """
        verifica que el usuario que quiere ingresar este en la base de datos, siendo asi le da acceso,
        de lo contrario no le permite el ingreso a la aplicacion
        :param cedula: Identificador para el ingreso
        :param contrasenia: Conntraseña para ese identificador
        :return:
        """
        cedula = self.buscar_usuario(cedula_usuario)
        contrasenia = self.buscar_contrasenia(cedula_usuario)

        if cedula != [] and contrasenia[0][0] == contraseniaUsuario:
            return (cedula, contraseniaUsuario)
        else:
            raise Usuario_o_ContraseniaIncorrecto(cedula, f"Usuario o contraseña incorrecto, porfavor intente nuevamente")

    def recuperar_contrasenia(self, cedula, correo, contraseniaNueva, confirmarContrasenia):
        """
        Metodo para la recuperacion de la contraseña del usuario, evalua que el usuario si exista y si la contraseña
        nueva es igual a la confirmacion de la contraseña
        :param cedula: identificador del usuario
        :param correo: correo del usuario
        :param contraseniaNueva: contraseña nueva del usuario
        :param confContrasenia: confirmacion de la contraseña
        :return: Actualiza la contraseña en la base de datos, si hay algun error mostrara un mensaje
        """

        busquedaUsuario = self.buscar_usuario(cedula)
        consultaActualizar = f"UPDATE Usuario SET contraseña = '{contraseniaNueva}' where id_usuario = '{cedula}'"

        if busquedaUsuario != [] and contraseniaNueva == confirmarContrasenia:
            self.c.update_in_database(consultaActualizar)
        elif busquedaUsuario != [] and contraseniaNueva != confirmarContrasenia:
            raise ContraseniasDiferentes(f"Las contraseñas no coinciden")
        else:
            raise UsuarioNoExistenteError(cedula, f"No existe ningun usuario con la cédula: {cedula}")

    def realizar_reserva(self, cedula, fecha, hora):
        """
        Metodo que actualiza la base de datos insertando una nueva fila en la tabla de reservas
        :param cedula: identificador del usuario
        :param fecha: fecha del dia de la reserva
        :param hora: hora de la reserva
        :return: actualiza la base de datos si hay cupos disponibles, sino muestra un error
        """

        consultaCupos = f"SELECT COUNT(id_usuario) FROM Reserva WHERE fecha = '{fecha}' AND hora = '{hora}'"
        consultaCrearReserva = f"INSERT INTO Reserva VALUES('{fecha}','{hora}', {cedula})"
        consultaBuscarReserva = f"SELECT * FROM Reserva WHERE id_usuario = '{cedula}' and fecha = '{fecha}'"
        cupos = self.c.select_in_database(consultaCupos)
        buscarReserva = self.c.select_in_database(consultaBuscarReserva)
        print(buscarReserva)
        if cupos[0][0] < 30 and buscarReserva == []:
            self.c.insert_in_database(consultaCrearReserva)
        else:
            raise ReservaExistenteError(cedula, f"Lo sentimos, usted ya tiene una reserva para el {fecha} a las {hora}")

    def cupos_disponibles_por_turno(self,fecha,hora):


        consulta = F"SELECT COUNT (id_usuario) FROM Reserva WHERE fecha = '{fecha}' and hora = '{hora}'"
        cuposTotales = 30
        cuposLleno =  self.c.select_in_database(consulta)

        return cuposTotales-cuposLleno[0][0]

    def cupos_disponibles_por_dia(self,fecha):

        consulta = F"SELECT COUNT (id_usuario) FROM Reserva WHERE fecha = '{fecha}'"
        cuposTotales = 210
        cuposLleno =  self.c.select_in_database(consulta)

        return cuposTotales-cuposLleno[0][0]

    def reservas_usuario_dia_actual(self,cedula,fecha):

        consulta = F"SELECT id_usuario, hora FROM Reserva WHERE fecha = '{fecha}' AND id_usuario = '{cedula}' "

        return self.c.select_in_database(consulta)

    def enviar_opinion(self, cedula, descripcion, fecha):

        consultaOpinion  = f"INSERT INTO Opinion VALUES('{cedula}', '{descripcion}', '{fecha}')"
        self.c.insert_in_database(consultaOpinion)


class Estudiante(Usuario):

    def __init__(self,cedula, nombre, edad, correo, telefono, contrasenia,programa):
        super().__init__(self,cedula, nombre, edad, correo, telefono, contrasenia)
        self.programa: str = programa

class EstDestacado(Estudiante):

    def __init__(self, cedula, nombre, edad, correo, telefono, contrasenia, programa,seleccion, deporte):
        super().__init__(self, cedula, nombre, edad, correo, telefono, contrasenia, programa)
        self.seleccion: str  = seleccion
        self.deporte: str = deporte


