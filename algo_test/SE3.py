import numpy as np
import quaternion


class SE3:
    def __init__(self):
#        self.transform_matrix = np.identity(4)
        self.rotation_quaternion = np.quaternion(0.0, 0.0, 0.0, 0.0)
        self.translation_vector = np.zeros(3)

    def SetTranslation(self, t):
        self.translation_vector = t

    def AddTraslation(self, t):
        self.translation_vector = self.translation_vector + t
