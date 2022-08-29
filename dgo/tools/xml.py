import xml.etree.ElementTree as ET
import os

class ImportXML():

    def __init__(self, url) -> None:
        url_file = url[7:]
        tree = None
        root = None
        self.open_xml(url_file)


    def open_xml(self, url):
        if not os.path.exists(url):
            print('ERROR : This file path does not exist !!!')
        else:
            print("Abrindo: ", url)
            self.tree = ET.parse(url)
            self.root = self.tree.getroot()

    def get_objects(self):
        pass
