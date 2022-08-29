
class ViewPort():

    def __init__(self, vpmin=0, vpmax=0) -> None:
        self.vpmin = vpmin
        self.vpmax = vpmax
    
    def set_dimension(self, vpmin, vpmax):
        self.vpmin = vpmin
        self.vpmax = vpmax
        