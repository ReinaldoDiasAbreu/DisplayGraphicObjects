import os
from pathlib import Path

from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QUrl, Slot, QObject

class Bridge(QObject):

    @Slot()
    def open_file(self):
        print("Open File...")


def start():
    app = QGuiApplication()
    engine = QQmlApplicationEngine()
    bridge = Bridge()
    context = engine.rootContext()
    context.setContextProperty('bridge', bridge)

    CURRENT_DIRECTORY = Path(__file__).resolve().parent
    filename = os.fspath(CURRENT_DIRECTORY / "gui" / "tela.qml")
    url = QUrl.fromLocalFile(filename)

    try:
        engine.load(url)
    except error:
        print(error)
    
    print("Start Aplication!")
    app.exec()


if __name__ == "__main__":
    start()
