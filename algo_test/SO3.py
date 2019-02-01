import numpy as np
import quaternion


class SO3:
    def __init__(self):
        self.rotation_quaternion = np.quaternion(1.0, 0.0, 0.0, 0.0)

    def init_with_axis_angle(self, angle, axis):
        ha = 0.5 * angle
        naxis = axis / np.linalg.norm(axis)

        self.rotation_quaternion = quaternion.quaternion(np.cos(ha),
                                                         np.sin(ha) * naxis[0],
                                                         np.sin(ha) * naxis[1],
                                                         np.sin(ha) * naxis[2])

    def apply_to_point(self, p):
        return self.rotation_quaternion * quaternion.quaternion(*p) * self.rotation_quaternion.inverse().vec
