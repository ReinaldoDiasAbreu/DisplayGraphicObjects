from .object import Object
from .ponto import Ponto

class Reta(Object):
    
    def __init__(self) -> None:
        super().__init__()
        self.points = []
    
    def get_points(self):
        return self.points
    
    def add_point(self, point):
        self.points.append(point)

    def get_list_points(self):
        points_list = []

        for p in self.points:
            ponto = []
            ponto.append(p.get_x())
            ponto.append(p.get_y())
            points_list.append(ponto)

        return points_list

    def __repr__(self):
        return f'Reta:[{self.points[0]}, {self.points[1]}]'
    