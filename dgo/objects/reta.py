from .object import Object
from .ponto import Ponto

class Reta(Object):
    
    def __init__(self) -> None:
        super().__init__()
        self.points = []
        self.tipo = 'reta'
    
    def add_point(self, x, y):
        point = Ponto(x, y)
        self.points.append(point)
