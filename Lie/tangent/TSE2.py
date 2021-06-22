import numpy as np

from Lie import SE2

class TSE2:
    def __init__(self, g:SE2, v):
        self.g = g
        if(len(v) == 3):
            self.v = np.reshape(v, (3,1))
        else:
            raise ValueError("Velocity is the wrong shape")
    
    def fiber(self):
        return self.v
    
    def base(self):
        return self.g
