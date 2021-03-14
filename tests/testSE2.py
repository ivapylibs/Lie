import numpy as np
import sys

sys.path.insert(1,'../')
from Lie import SE2

theta = np.pi/2
R = np.array([[np.cos(theta), -np.sin(theta)], 
                [np.sin(theta), np.cos(theta)]])
x = np.array([[1], [0]])
a = SE2.SE2(R=R, x=x)

theta = -np.pi/2
R = np.array([[np.cos(theta), -np.sin(theta)], 
                [np.sin(theta), np.cos(theta)]])
x = np.array([[0], [1]])

b = SE2.SE2(R=R, x=x)

print(a)
print(b)
print(a*b)