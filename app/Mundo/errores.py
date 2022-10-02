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