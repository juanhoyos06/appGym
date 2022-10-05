from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from app.Mundo import mundo
from app.Mundo.mundo import Usuario

class Ui(ScreenManager):
    pass


class MainApp(MDApp):

    def __init__(self):
        super().__init__()
        self.mundo = mundo
        self.usuario = Usuario()

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"
        Builder.load_file('design.kv')

        return Ui()

    def iniciar_sesion(self, cedula, contraseniaUsuario):
        self.usuario.iniciar_sesion(cedula, contraseniaUsuario)

    def crear_usuario(self,cedula, nombre, edad, sexo, correo, telefono, contrasenia, cargo):
        self.usuario.crear_usuario(cedula, nombre, edad, sexo, correo, telefono, contrasenia, cargo)

    def recuperar_contrasenia(self, cedula, contraseniaNueva, confirmarContrasenia):
        self.usuario.recuperar_contrasenia(cedula, contraseniaNueva, confirmarContrasenia)

    def realizar_reserva(self,cedula, fecha, hora):
        self.usuario.realizar_reserva(cedula, fecha, hora)


if __name__ == '__main__':
    MainApp().run()