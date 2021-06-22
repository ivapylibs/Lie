import numpy as np
from Lie import SE2

theta = np.pi/3
R = SE2.rotationMatrix(theta)
x = np.array([[1], [0]])
a = SE2(R=R, x=x)

theta = -np.pi/2
R = SE2.rotationMatrix(theta)
x = np.array([[0], [1]])

b = SE2(R=R, x=x)

c = np.array([0,1])

print(a)
print(b)
print(a*b)
print(a*c)
print(a.inv() * a)