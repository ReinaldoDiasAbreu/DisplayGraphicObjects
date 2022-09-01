
class Window():

    def __init__(self, wmin=0, wmax=0) -> None:
        self.wmin = wmin
        self.wmax = wmax
    
    
    def __repr__(self):
        return f'WMin = {self.wmin} | WMax = {self.wmax}'
        