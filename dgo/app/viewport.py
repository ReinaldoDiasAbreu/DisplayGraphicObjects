
class ViewPort():

    def __init__(self, vpmin=0, vpmax=0) -> None:
        self.vpmin = vpmin
        self.vpmax = vpmax
    
    def get_vpmin(self):
        return self.vpmin
    
    def get_vpmax(self):
        return self.vpmax
        
    def __repr__(self):
        return f'VpMin = {self.vpmin} | VpMax = {self.vpmax}'
        