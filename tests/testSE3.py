import numpy as np
from Lie import SE3

roll = np.pi/3
pitch = np.pi/4
yaw = np.pi/6
#roll = np.pi/2
#pitch = 0
#yaw = 0

R = np.matmul(np.matmul(SE3.RotZ(yaw), SE3.RotY(pitch)), SE3.RotX(roll))

x = np.array([[1], [0], [0]])
a = SE3(R=R, x=x)

print("Commanded Roll, Pitch, and Yaw Angles:")
print((roll, pitch, yaw))
print("Calculated Roll, Pitch, and Yaw Angles:")
print(a.getRPY())

roll2 = np.pi/6
pitch2 = np.pi/3
yaw2 = np.pi/4

R2 = np.matmul(np.matmul(SE3.RotZ(yaw2), SE3.RotY(pitch2)), SE3.RotX(roll2))
x = np.array([[0],[0], [1]])

b = SE3(R=R, x=x)

c = np.array([0,0,1])

print(a)
print(b)
print(a*b)
print(a*c)

print(a.log())