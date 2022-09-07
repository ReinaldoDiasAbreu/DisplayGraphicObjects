import sys
import os

# Importa o QtCore
from .qt_core import *

# Importa a main window
from .gui.ui_main_window import UI_MainWindow
from .objects import *
from .tools.xml import ImportXML


class MainWindow(QMainWindow):


    def __init__(self) -> None:
        super().__init__()

        self.xml_file = ImportXML()
        
        # Definindo título para a aplicação
        self.setWindowTitle("Display Graphic Objects")

        # Setup da mainwindow
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # Ações
        self.ui.btn_open_file.clicked.connect(self.open_file)
        
        # Exibe Aplicação
        self.show()

    
    @Slot()
    def open_file(self):
        self.xml_file.open_file(self)
        print(self.xml_file.get_viewport())
        self.ui.define_objects(
            window_data=self.xml_file.get_window(), 
            viewport_data=self.xml_file.get_viewport(), 
            objects_data=self.xml_file.get_objects()
        )    


def start():
    print("Start Aplication!")
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
    