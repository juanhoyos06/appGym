import sys
from PySide2.QtWidgets import QApplication
from app.Mundo.mundo import *
from app.Vista.gui.gui import VentanaLogin

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gym = Gym()
    window = VentanaLogin(gym)
    sys.exit(app.exec_())