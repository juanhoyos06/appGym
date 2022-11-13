class GymError(Exception):
    pass

class UsuarioExistenteError(GymError):
    """
    Representa una excepción que indica que el usuario ya existe en la base de datos

    Attributes:
        cedula: un str que indica la cédula del socio que no existe
        msg: un str que contiene el mensaje de error
    """
    def __init__(self, cedula: str, msg: str):

        self.cedula = cedula
        self.msg = msg

class UsuarioNoExistenteError(GymError):
    """
    Representa una excepción que indica que el usuario no existe en la base de datos

    Attributes:
        cedula: un str que indica la cédula del socio que no existe
        msg: un str que contiene el mensaje de error
    """
    def __init__(self, cedula: str, msg: str):

        self.cedula = cedula
        self.msg = msg

class Usuario_o_ContraseniaIncorrecto(GymError):
    """
    Representa una excepción que indica que el usuario ya existe en la base de datos

    Attributes:
        cedula: un str que indica la cédula del socio que no existe
        msg: un str que contiene el mensaje de error
    """

    def __init__(self, cedula: str, msg: str):
        self.cedula = cedula
        self.msg = msg

class ContraseniasDiferentes(GymError):
    """
        Representa una excepción que indica que las contraseñas no coinciden

        Attributes:
            cedula: un str que indica la cédula del socio que no existe
            msg: un str que contiene el mensaje de error
        """

    def __init__(self, msg: str):
        self.msg = msg

class CorreoInvalido(GymError):
    """
        Representa una excepción que indica que el correo no es valido, no contiene '@'

        Attributes:

            msg: un str que contiene el mensaje de error
        """

    def __init__(self, msg: str):
        self.msg = msg

class ErrorMultiple(GymError):
    """
        Representa una excepción que indica que el correo no es valido, no contiene '@'
        y las contraseñas no coinciden

        Attributes:

            msg: un str que contiene el mensaje de error
        """

    def __init__(self, msg: str):
        self.msg = msg

class LimiteCupos(GymError):
    """
        Representa una excepción que indica que ya no hay cupos para reservar

        Attributes:
            cedula: un str que indica la cédula del socio que no existe
            msg: un str que contiene el mensaje de error
        """

    def __init__(self, msg: str):
        self.msg = msg

class ReservaExistenteError(GymError):
    """
    Representa una excepción que indica que el usuario ya tiene una reserva ese dia

    Attributes:
        cedula: un str que indica la cédula del socio que no existe
        msg: un str que contiene el mensaje de error
    """
    def __init__(self, cedula: str, msg: str):

        self.cedula = cedula
        self.msg = msg


class ReservaNoExistenteError(GymError):
    """
    Representa una excepción que indica que el usuario ya tiene una reserva ese dia

    Attributes:
        cedula: un str que indica la cédula del socio que no existe
        msg: un str que contiene el mensaje de error
    """
    def __init__(self, cedula: str, msg: str):

        self.cedula = cedula
        self.msg = msg