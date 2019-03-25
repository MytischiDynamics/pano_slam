import numpy as np
import quaternion


class SO3:
    def __init__(self):
        self.rotation_quaternion = np.quaternion(1.0, 0.0, 0.0, 0.0)

    def __mul__(self, other):
        result = SO3()
        result.init_with_quaternion(self.rotation_quaternion * other.rotation_quaternion)
        return result

    def init_with_quaternion(self, q):
        self.rotation_quaternion = q

    def init_with_axis_angle(self, axis, angle):
        ha = 0.5 * angle
        naxis = axis / np.linalg.norm(axis)

        self.rotation_quaternion = quaternion.quaternion(np.cos(ha),
                                                         np.sin(ha) * naxis[0],
                                                         np.sin(ha) * naxis[1],
                                                         np.sin(ha) * naxis[2])

    def apply_to_vector(self, p):
        return self.rotation_quaternion * quaternion.quaternion(*p) * self.rotation_quaternion.inverse()

    def get_quaternion(self):
        return self.rotation_quaternion

    def get_matrix(self):
        return quaternion.as_rotation_matrix(self.rotation_quaternion)

    def test_SO3(self):
        rot_trans = SO3()
        rot_trans.init_with_axis_angle(np.array([0.0, 0.0, 1.0]), np.pi / 4.0)
        print(str(rot_trans.apply_to_vector(np.array([1.0, 0.0, 0.0]))))
        new_rot_trans = rot_trans * rot_trans
        print(str(new_rot_trans.apply_to_vector(np.array([1.0, 0.0, 0.0]))))
        print(str(new_rot_trans.get_matrix()))
    #    transform = SE3.SO3()
    #    transform.init_with_axis_angle(0.1, np.array([1.0, 1.0, 1.0]))
    #    new_p = transform.apply_to_point(np.array([1.0, 1.0, 0.0]))
    #    print(str(new_p))
