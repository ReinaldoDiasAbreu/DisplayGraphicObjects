from ..objects.window import Window
from ..objects.viewport import ViewPort
from ..objects.ponto import Ponto
from ..objects.reta import Reta
from ..objects.poligono import Poligono


import xml.etree.ElementTree as ET
import os

class ImportXML():

    def __init__(self, url) -> None:
        url_file = url[7:]
        self.tree = None
        self.root = None
        self.open_xml(url_file)
        self.objects = []
        self.window = None
        self.viewport = None


    def open_xml(self, url):
        if not os.path.exists(url):
            print('ERROR : This file path does not exist !!!')
        else:
            print("Abrindo: ", url)
            self.tree = ET.parse(url)
            self.root = self.tree.getroot()


    def read_objects(self):
        for obj in self.root:
            match obj.tag:
                case 'viewport':
                    vp = ViewPort()
                    min = obj.get('vpmin')
                    max = obj.get('vpmmax')
                    vp.set_dimension(min, max)
                    self.viewport = vp
                case 'Window':
                    win = Window()
                    min = obj.get('wmin')
                    max = obj.get('wmmax')
                    win.set_dimension(min, max)
                    self.window = win
                case 'ponto':
                    point = Ponto()
                    x = obj.get('x')
                    y = obj.get('y')
                    point.set_point(x, y)
                    self.objects.append(point)
                case 'reta':
                    reta = Reta()
                    for obj_child in obj:
                        x = obj_child.get('x')
                        y = obj_child.get('y')
                        reta.add_point(x, y)
                    self.objects.append(reta)
                case 'poligono':
                    poligono = Poligono()
                    for obj_child in obj:
                        x = obj_child.get('x')
                        y = obj_child.get('y')
                        poligono.add_point(x, y)
                    self.objects.append(poligono)


    def get_list(self):

        list_objects = []

        for obj in self.objects:
            match obj.tipo:
                case 'ponto':
                    point = ['ponto',obj.x, obj.y]
                    list_objects.append(point)
                case 'reta':
                    reta = ['reta']
                    for obj_child in obj.points:
                        point = [obj_child.x, obj_child.y]
                        reta.append(point)
                    list_objects.append(reta)
                case 'poligono':
                    poligono = ['poligono']
                    for obj_child in obj.points:
                        point = [obj_child.x, obj_child.y]
                        poligono.append(point)
                    list_objects.append(poligono)
        
        return list_objects


    def __str__(self) -> str:
        return (f'{len(self.objects)} Objects')
    

