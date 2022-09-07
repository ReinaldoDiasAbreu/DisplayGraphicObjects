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
        self.ui.btn_save_file.clicked.connect(self.save_file)
        self.ui.btn_clear.clicked.connect(self.clear)
        
        # Exibe Aplicação
        self.show()

    
    @Slot()
    def open_file(self):
        self.xml_file.open_file(self)
        n_objs = self.xml_file.get_num_objects()
        if n_objs > 0:
            self.ui.bottom_label_left.setText(f"Show {n_objs} objects!")

        print(self.xml_file.get_viewport())
        print(self.xml_file.get_window())
        
        self.ui.define_objects(
            window_data=self.xml_file.get_window(), 
            viewport_data=self.xml_file.get_viewport(), 
            objects_data=self.xml_file.get_objects()
        )
    
    @Slot()
    def save_file(self):
        file_path = QFileDialog().getSaveFileName(parent=self.ui.content, caption='Save File')
        print("Save coordinates...", end="")
        if len(file_path[0]) > 0:
            file = open(file_path[0], "w")
            if self.ui.obj_coord is not None:
                for obj in self.ui.obj_coord:
                    file.write(str(obj)+"\n")
            file.close()
            print("OK!")
        else:
            print("Erro!")
    
    @Slot()
    def clear(self):
        self.ui.view_objects.clear()
        self.ui.view_objects.update()


def start():
    print("Start Aplication!")
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
    