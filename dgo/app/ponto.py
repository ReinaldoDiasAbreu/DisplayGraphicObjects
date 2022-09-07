from .object import Object

class Ponto(Object):
    
    def __init__(self, x=0, y=0) -> None:
        super().__init__()
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
        
    def __repr__(self):
        return f'Ponto:({self.x}, {self.y})'
