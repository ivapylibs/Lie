import numpy as np
import Lie.group.SE3.Homog

roll = np.pi/3
pitch = np.pi/4
yaw = np.pi/6
#roll = np.pi/2
#pitch = 0
#yaw = 0

R = np.matmul(np.matmul(Lie.group.SE3.Homog.RotZ(yaw), Lie.group.SE3.Homog.RotY(pitch)), Lie.group.SE3.Homog.RotX(roll))

x = np.array([[1], [0], [0]])
a = Lie.group.SE3.Homog(R=R, x=x)

print("Commanded Roll, Pitch, and Yaw Angles:")
print((roll, pitch, yaw))
print("Calculated Roll, Pitch, and Yaw Angles:")
print(a.getRPY())

roll2 = np.pi/6
pitch2 = np.pi/3
yaw2 = np.pi/4

R2 = np.matmul(np.matmul(Lie.group.SE3.Homog.RotZ(yaw2), Lie.group.SE3.Homog.RotY(pitch2)), Lie.group.SE3.Homog.RotX(roll2))
x = np.array([[0],[0], [1]])

b = Lie.group.SE3.Homog(R=R, x=x)

c = np.array([0,0,1])

print(a)
print(b)
print(a*b)
print(a*c)

print(a.log())