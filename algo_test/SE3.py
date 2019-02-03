import numpy as np
from SO3 import SO3


class SE3:
    def __init__(self):
        self.so3 = SO3()
        self.translation_vector = np.zeros(3)

    def __mul__(self, other):
        result = SE3()
        result.set_rotation(self.so3 * other.so3)
        result.set_translation(self.get_translation() + self.get_rotation().apply_to_vector(other.get_translation()))
        return result

    def get_translation(self):
        return self.translation_vector

    def set_translation(self, t):
        self.translation_vector = t

    def set_rotation(self, q):
        self.so3.init_with_quaternion(q)

    def get_rotation(self):
        return self.so3

    def get_matrix(self):
        bot_vec = np.array([0.0, 0.0, 0.0, 1.0])
        ret_m = np.hstack((self.get_rotation().get_matrix(), np.transpose(self.get_translation())))
        ret_m = np.vstack((ret_m, bot_vec))
        return ret_m

