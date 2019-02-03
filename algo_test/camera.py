import SE3
from point_cloud import Point
import numpy as np


class Camera:
    def __init__(self):
        self.camera_extrinsics = SE3.SE3()
        self.camera_intrinsics = CameraIntrinsics()
        self.projection_matrix = np.zeros((4, 4))

    def get_translation(self):
        return self.camera_extrinsics.get_translation()

    def set_translation(self, t):
        self.camera_extrinsics.set_translation(t)

    def get_rotation(self):
        self.camera_extrinsics.get_rotation()

    def set_rotation(self, q):
        self.camera_extrinsics.set_rotation(q)

    def set_extrinsics(self, transform):
        self.camera_extrinsics = transform

    def generate_projection_matrix(self):
        cam_to_film = np.hstack((np.identity(3), np.transpose(np.zeros(3))))
        self.projection_matrix = self.camera_intrinsics.get_camera_matrix() * \
                                 cam_to_film * \
                                 self.camera_extrinsics.get_matrix()
        return self.projection_matrix

    def calculate_projection(self, p):
        ret_p = Point()
        ret_p.set_homogeneous_coords(self.projection_matrix() * p.get_homogeneous_coords())
        return ret_p


class CameraIntrinsics:
    def __init__(self):
        self.camera_matrix = np.zeros((3, 3))
        self.distortion_coeffs = np.zeros(1)

    def set_camera_matrix(self, K):
        self.camera_matrix = K
#       self.camera_matrix[1, 1] = -self.camera_matrix[1, 1]

    def get_camera_matrix(self):
        return self.camera_matrix
