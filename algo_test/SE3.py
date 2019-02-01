import numpy as np
import quaternion
from SO3 import SO3


class SE3:
    def __init__(self):
        self.so3 = SO3()
        self.translation_vector = np.zeros(3)

    def GetTranslation(self):
        return self.translation_vector

    def SetTranslation(self, t):
        self.translation_vector = t


'''
    def AddTraslation(self, t):
        self.translation_vector = self.translation_vector + t

    def GetRotation(self):
        return self.rotation_quaternion

    def SetRotation(self, axis, angle):

'''
#    def AddRotation(self, q):
