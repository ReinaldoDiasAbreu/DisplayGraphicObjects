from .object import Object

class Ponto(Object):
    
    def __init__(self, x=0, y=0) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.tipo = 'ponto'
    
    def set_point(self, x, y):
        self.x = x
        self.y = y
