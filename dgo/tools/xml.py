import imp
from ..objects.window import Window
from ..objects.viewport import ViewPort
from ..objects.ponto import Ponto
from ..objects.reta import Reta
from ..objects.poligono import Poligono

from ..qt_core import *

import xml.etree.ElementTree as ET
import os

class ImportXML():

    def __init__(self) -> None:
        self.url_file = None
        self.tree = None
        self.root = None
        self.objects = []
        self.window = None
        self.viewport = None


    def open_xml(self, url):
        try:
            self.url_file = url
            self.tree = ET.parse(url)
            self.root = self.tree.getroot()
        except:
             print('ERROR: This file path does not exist !!!')

    def read_objects(self):
        if self.root is not None:
            for obj in self.root:
                match obj.tag:
                    case 'viewport':
                        vp = ViewPort()
                        vp.vpmin = [float(obj[0].get('x')), float(obj[0].get('y'))]
                        vp.vpmax = [float(obj[1].get('x')), float(obj[1].get('y'))]
                        self.viewport = vp
                    case 'Window':
                        win = Window()
                        win.wmin = [float(obj[0].get('x')), float(obj[0].get('y'))]
                        win.wmax = [float(obj[1].get('x')), float(obj[1].get('y'))]
                        self.window = win
                    case 'ponto':
                        point = Ponto()
                        point.x = obj.get('x')
                        point.y = obj.get('y')
                        self.objects.append(point)
                    case 'reta':
                        reta = Reta()
                        for obj_child in obj:
                            point = Ponto()
                            point.x = obj_child.get('x')
                            point.y = obj_child.get('y')
                            reta.points.append(point)
                        self.objects.append(reta)
                    case 'poligono':
                        poligono = Poligono()
                        for obj_child in obj:
                            point = Ponto()
                            point.x = obj_child.get('x')
                            point.y = obj_child.get('y')
                            poligono.points.append(point)
                        self.objects.append(poligono)

    def open_file(self, parent):
        print("Open XML File... ", end="")
        file_path = QFileDialog().getOpenFileName(parent=parent, caption='Open XML File', filter='*.xml')
        if len(file_path[0]) > 0:
            self.open_xml(file_path[0])
            self.read_objects()
            print("OK!")
        else:
            print("Erro!")

    def get_window(self):
        return self.window
    
    def get_viewport(self):
        return self.viewport
    
    def get_objects(self):
        return self.objects

    def __str__(self) -> str:
        return (f'Read {len(self.objects)} objects.')
    

