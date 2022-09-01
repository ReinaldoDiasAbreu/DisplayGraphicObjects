from mimetypes import init
from PySide6 import QtCore, QtGui, QtWidgets
from ..tools.xml import ImportXML

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Display Graphic Objects")
        self.setFixedSize(QtCore.QSize(1366, 768))
        self.setLayout(QtWidgets.QHBoxLayout())
        self.start_elements()
        
    def start_elements(self):
        """
        Iniciando elementos da janela principal.
        """
        self.init_menu()

    def init_menu(self):
        """
        Iniciar os objetos do menu.
        """
        self.toolbar = self.addToolBar('File')
        button_action = QtGui.QAction("Open File", self)
        button_action.setStatusTip("Open XML file.")
        button_action.triggered.connect(self.open_xml_file)
        self.toolbar.addAction(button_action)

    def open_xml_file(self):
        print("Open XML File.")
        file_path = QtWidgets.QFileDialog().getOpenFileName(parent=self, dir='/', caption='Open XML File', filter='*.xml')
        if len(file_path[0]) > 0:
            xml_file = ImportXML()
            xml_file.open_xml(file_path[0])
            xml_file.read_objects()
            print(xml_file)
