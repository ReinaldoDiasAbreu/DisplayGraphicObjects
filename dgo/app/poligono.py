from .object import Object
from .ponto import Ponto

class Poligono(Object):
    
    def __init__(self) -> None:
        super().__init__()
        self.points = []

    
    def get_list_points(self):
        points_list = []

        for p in self.points:
            ponto = []
            ponto.append(p.get_x())
            ponto.append(p.get_y())
            points_list.append(ponto)

        return points_list
    
    
    def add_point(self, point):
        self.points.append(point)
    

    def __repr__(self):
        return f'Poligono:{str(self.points)}'
    
    