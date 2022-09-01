from .object import Object

class Ponto(Object):
    
    def __init__(self, x=0, y=0) -> None:
        super().__init__()
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'({self.x}, {self.y})'
