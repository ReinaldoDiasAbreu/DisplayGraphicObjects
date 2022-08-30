
class Window():

    def __init__(self, wmin=0, wmax=0) -> None:
        self.wmin = wmin
        self.wmax = wmax
        self.tipo = 'window'
    
    def set_dimension(self, wmin, wmax):
        self.wmin = wmin
        self.wmax = wmax
    
    def __str__(self) -> str:
        return "Window"