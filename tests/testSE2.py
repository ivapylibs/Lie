from Lie.group.SE3 import Homog
import numpy as np
import Lie.group.SE2.Homog

theta = np.pi/3
R = Lie.group.SE2.Homog.rotationMatrix(theta)
x = np.array([[1], [0]])
a = Lie.group.SE2.Homog(R=R, x=x)

theta = -np.pi/2
R = Lie.group.SE2.Homog.rotationMatrix(theta)
x = np.array([[0], [1]])

b = Lie.group.SE2.Homog(R=R, x=x)

c = np.array([0,1])

print(a)
print(b)
print(a*b)
print(a*c)
print(a.inv() * a)