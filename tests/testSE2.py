#!/usr/bin/python3
#=========================== testSE2 ===========================
#
# @brief    Code to test basic multiplication functionality of SE2
#
#=========================== testSE2 ===========================

#
# @file     testSE2.py
#
# @author   Yunzhi Lin, yunzhi.lin@gatech.edu
# @date     2021/07/13 [modified]
#
# @quit
#=========================== testSE2 ===========================

#==[0] Prep environment
#
import numpy as np
import Lie.group.SE2.Homog

#==[1] Test Homog objects multiplication
#
theta = 0
R = Lie.group.SE2.Homog.rotationMatrix(theta)
x = np.array([[200], [200]])
a = Lie.group.SE2.Homog(R=R, x=x)

theta = -np.pi/2
R = Lie.group.SE2.Homog.rotationMatrix(theta)
x = np.array([[0], [1]])

b = Lie.group.SE2.Homog(R=R, x=x)

print('Test Homog objects multiplication')
print('Homog object:\n', a)
print('Homog object:\n', b)
print('Result:\n', a*b)
print('\n')

#==[2] Test Homog object multiplication with point
#
b = np.array([-12, 18])

print('Test Homog object multiplication with point')
print('Homog object:\n', a)
print('Point:\n', b)
print('Result:\n', a*b)
print('\n')

#==[3] Test Homog object multiplication with velocity
#
b = np.array([-12,18,1])

print('Test Homog object multiplication with velocity')
print('Homog object:\n', a)
print('Velocity:\n', b)
print('Result:\n', a*b)
print('\n')

#==[4] Test Homog object multiplication with 2D matrix of points
#
b = np.array([[-12,18],[18,18]])

print('Test Homog object multiplication with 2D matrix of points')
print('Homog object:\n', a)
print('2D matrix of points:\n', b)
print('Result:\n', a*b)
print('\n')

#==[5] Test Homog object multiplication with 2D matrix of velocities
#
b = np.array([[-12,18],[18,18],[1,1]])

print('Test Homog object multiplication with 2D matrix of velocities')
print('Homog object:\n', a)
print('2D matrix of velocities:\n', b)
print('Result:\n', a*b)
print('\n')

#
#=========================== testSE2 ============================