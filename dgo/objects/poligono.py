from .object import Object
from .ponto import Ponto

class Poligono(Object):
    
    def __init__(self) -> None:
        super().__init__()
        self.points = []
    
    def add_point(self, x, y):
        point = Ponto(x, y)
        self.points.append(point)