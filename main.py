import sys
import time
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QButtonGroup
from PySide6.QtCore import QFile, QIODevice , Qt
import funciones

def leer():
    mac_ip = funciones.leerControler()
    window.mac.setText(mac_ip[0])
    window.ip.setText(mac_ip[1])
    print(mac_ip)

def salir():
    print("salir")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_file_name = "main.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    window.leer.clicked.connect(lambda : leer())
    window.salir.clicked.connect(lambda : salir())
    
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()

    sys.exit(app.exec())