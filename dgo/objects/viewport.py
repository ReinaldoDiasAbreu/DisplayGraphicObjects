
class ViewPort():

    def __init__(self, vpmin=0, vpmax=0) -> None:
        self.vpmin = vpmin
        self.vpmax = vpmax
    
    def __repr__(self):
        return f'VpMin = {self.vpmin} | VpMax = {self.vpmax}'
        