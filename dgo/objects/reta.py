from .object import Object
from .ponto import Ponto

class Reta(Object):
    
    def __init__(self, points = []) -> None:
        super().__init__()
        self.points = points

    def __repr__(self):
        return f'P1 = {self.points[0]} | P2 = {self.points[1]}'
    