import os
from pathlib import Path
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QUrl, Slot, QObject
from .tools.xml import ImportXML

class Bridge(QObject):

    @Slot(str)
    def open_file(self, file_url):
        xml = ImportXML(file_url)


class Window(QGuiApplication):

    def __init__(self):
        super().__init__()
    
        engine = QQmlApplicationEngine()
        bridge = Bridge()
        context = engine.rootContext()
        context.setContextProperty('bridge', bridge)

        CURRENT_DIRECTORY = Path(__file__).resolve().parent
        filename = os.fspath(CURRENT_DIRECTORY / "gui" / "tela.qml")
        url = QUrl.fromLocalFile(filename)

        engine.load(url)
        
        print("Start Aplication!")
        self.exec()


def start():
    win = Window()


if __name__ == "__main__":
    start()
