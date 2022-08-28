import os
from pathlib import Path
import sys

from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QUrl


def start():
    app = QGuiApplication()
    engine = QQmlApplicationEngine()

    CURRENT_DIRECTORY = Path(__file__).resolve().parent
    filename = os.fspath(CURRENT_DIRECTORY / "gui" / "tela.qml")
    url = QUrl.fromLocalFile(filename)

    engine.load(url)
    print("Start Aplication!")
    app.exec()
