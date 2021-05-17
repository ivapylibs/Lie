import numpy as np


class SE2:
    def __init__(self, *args, **kwargs):
        if(len(kwargs) == 0):
            self.__M = np.eye(3)
        elif(len(kwargs) == 2):
            R = kwargs['R']
            x = kwargs['x']
            if(np.shape(R) != (2,2)):
                raise ValueError("Rotation Matrix must be orthogonal 2x2 matrix")
            if(np.shape(x) != (2,1)):
                raise ValueError("Displacement must be 2x1 vector")

            self.__M = np.hstack((R, x))
            self.__M = np.vstack((self.__M, np.array([0,0,1])))
        elif(len(kwargs) == 1):
            M = kwargs['M']
            if(np.shape(M) == (3,3) and np.array_equal(M[2,:], np.array([0, 0, 1]))):
                self.__M = M
            else:
                raise ValueError("Not a Homogenous matrix")
    
    def getTranslation(self):
        return self.__M[0:2, 2][:,np.newaxis]
    
    def getRotation(self):
        return self.__M[0:2, 0:2]
    
    def getAngle(self):
        return np.arctan2(self.__M[1,0], self.__M[0,0])
    
    def inv(self):
        return SE2(M=np.linalg.inv(self.__M))


    def __mul__(self, other):
        if(type(other) == SE2):
            m = np.matmul(self.__M, other.__M)
            return SE2(M=m)
        elif(type(other) == np.ndarray):
            if(np.shape(np.squeeze(other)) == (2,)): # Point
                otherS = np.squeeze(other)
                vec = np.vstack((otherS[:, np.newaxis], [1]))
                return np.matmul(self.__M, vec)[:-1]
            elif(np.shape(np.squeeze(other)) == (3,)): # Velocity
                L = np.eye(3)
                L[0:2,0:2] = self.__M[0:2,0:2]
                return np.matmul(L, other)


    
    def __str__(self):
        return str(self.__M)

    @staticmethod
    def rotationMatrix(theta):
        return np.squeeze(np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]))