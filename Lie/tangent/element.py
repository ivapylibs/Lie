import numpy as np


class Element:
    def __init__(self, g, v):
        self.g = g
        self.v = v
    
    def fiber(self):
        return self.v
    
    def base(self):
        return self.g
