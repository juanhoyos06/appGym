from app.Mundo.conexion import Conexion
from app.Mundo.errores import *

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

    def buscar_usuario(self, cedula):
        """
        Se encarga de buscar si un usuario esta dentro de la base de datos

        :param cedula: Identificador del usuario
        :return: El identificador del usuario en una lista si el usuario existe, si no, la lista estara vacia
        """

        consulta = f"SELECT id_usuario FROM Usuario WHERE id_usuario = '{cedula}'"
        return self.c.select_in_database(consulta)

    def crear_usuario(self,cedula, nombre, edad, sexo, correo, telefono, contrasenia, cargo):
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


        if self.buscar_usuario(cedula) == []:
            self.c.insert_in_database(consultaInsert)
        else:
            raise UsuarioExistenteError(cedula, f"Ya existe un usuario con la cedula{cedula}")

    def buscar_contrasenia(self, cedula):
        """
        Se encarga de buscar la contraseña del usuario
        :param cedula: Identificador del usuario
        :return: La contraseña del usuario en una lista si el usuario existe, si no, la lista estara vacia
        """
        consulta = f"SELECT contrasenia FROM Usuario WHERE id_usuario = '{cedula}'"
        return self.c.select_in_database(consulta)

    def iniciar_sesion(self, cedula, contraseniaUsuario):
        """
        verifica que el usuario que quiere ingresar este en la base de datos, siendo asi le da acceso,
        de lo contrario no le permite el ingreso a la aplicacion
        :param cedula: Identificador para el ingreso
        :param contrasenia: Conntraseña para ese identificador
        :return:
        """
        cedula = self.buscar_usuario(cedula)
        contrasenia = self.buscar_contrasenia(cedula)

        if cedula != [] and contrasenia[0][0] == contraseniaUsuario:
            return (cedula, contraseniaUsuario)
        else:
            raise Usuario_o_ContraseniaIncorrecto(cedula, f"Usuario o contraseña incorrecto, porfavor intente nuevamente")

class Estudiante(Usuario):

    def __init__(self,cedula, nombre, edad, correo, telefono, contrasenia,programa):
        super().__init__(self,cedula, nombre, edad, correo, telefono, contrasenia)
        self.programa: str = programa

class EstDestacado(Estudiante):

    def __init__(self, cedula, nombre, edad, correo, telefono, contrasenia, programa,seleccion, deporte):
        super().__init__(self, cedula, nombre, edad, correo, telefono, contrasenia, programa)
        self.seleccion: str  = seleccion
        self.deporte: str = deporte


