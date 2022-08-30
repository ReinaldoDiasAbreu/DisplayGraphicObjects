
class ViewPort():

    def __init__(self, vpmin=0, vpmax=0) -> None:
        self.vpmin = vpmin
        self.vpmax = vpmax
        self.tipo = 'viewport'
    
    def set_dimension(self, vpmin, vpmax):
        self.vpmin = vpmin
        self.vpmax = vpmax
    
    def __str__(self) -> str:
        return "ViewPort"
        