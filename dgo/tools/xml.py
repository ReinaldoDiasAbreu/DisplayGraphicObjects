from ..objects.window import Window
from ..objects.viewport import ViewPort
from ..objects.ponto import Ponto
from ..objects.reta import Reta
from ..objects.poligono import Poligono


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
                        vp.vpmin = obj.get('vpmin')
                        vp.vpmax = obj.get('vpmmax')
                    case 'Window':
                        win = Window()
                        win.wmin = obj.get('wmin')
                        win.wmax = obj.get('wmmax')
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


    def __str__(self) -> str:
        return (f'Read {len(self.objects)} objects.')
    

