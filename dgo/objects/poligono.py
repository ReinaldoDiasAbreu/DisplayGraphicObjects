from .object import Object
from .ponto import Ponto

class Poligono(Object):
    
    def __init__(self, lista_pontos = []) -> None:
        super().__init__()
        self.points = lista_pontos
    
    def __repr__(self):
        return f'Pontos = {str(self.points)}'
    
    