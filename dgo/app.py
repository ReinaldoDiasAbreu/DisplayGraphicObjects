import sys
from PySide6 import QtCore, QtGui, QtWidgets
from .gui.main_win import MainWindow

window = None

def start():
    print("Start Aplication!")
    app = QtWidgets.QApplication()
    app.setStyleSheet('Material')
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
