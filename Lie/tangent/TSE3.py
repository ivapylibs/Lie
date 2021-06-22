import numpy as np

from Lie import SE3

class TSE2:
    def __init__(self, g:SE3, v):
        self.g = g
        if(len(v) == 6):
            self.v = np.reshape(v, (6,1))
        else:
            raise ValueError("Velocity is the wrong shape")
    
    def fiber(self):
        return self.v
    
    def base(self):
        return self.g
