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
#       cam_to_film = np.hstack((np.identity(3), np.transpose(np.zeros(3))))
#       self.projection_matrix = self.camera_intrinsics.get_camera_matrix() * \
#                                cam_to_film * \
#                                self.camera_extrinsics.get_matrix()
        self.projection_matrix = self.camera_intrinsics.get_camera_matrix() * \
                                 self.camera_extrinsics.get_matrix()
        return self.projection_matrix

    def projection(self, p):
        ret_p = Point()
#       with this operation we get point projection on camera
#       Structure of resulting vector is (x, y, 1, d)
#       For more information see Microsoft "Image alignment and stitching tutorial"
        projection_vector = self.projection_matrix() * p.get_homogeneous_coords()
        ret_p.set_homogeneous_coords(projection_vector[0:1])
        return ret_p

    def inverse_projection(self, p, i_depth):
        ret_p = Point()
        extended_vector = np.hstack(p.get_homogeneous_coords, np.array([1.0 / i_depth]))
        res_p = np.linalg.inv(self.camera_extrinsics.get_matrix()) *\
                np.linalg.inv(self.camera_intrinsics.get_camera_matrix()) *\
                extended_vector
        ret_p.set_homogeneous_coords(res_p[:2])
        return ret_p


class CameraIntrinsics:
    def __init__(self):
        self.camera_matrix = np.zeros((4, 4))
        self.camera_matrix[2, 2] = 1.0
        self.camera_matrix[3, 3] = 1.0
        self.distortion_coeffs = np.zeros(1)

#   camera matrix is for homogeneous coordinates
    def set_camera_matrix(self, K):
        self.camera_matrix = K
#       self.camera_matrix[1, 1] = -self.camera_matrix[1, 1]

    def get_camera_matrix(self):
        return self.camera_matrix

    def set_fx(self, fx):
        self.camera_matrix[0, 0] = fx

    def get_fx(self):
        return self.camera_matrix[0, 0]

    def set_fy(self, fy):
        self.camera_matrix[1, 1] = fy

    def get_fy(self):
        return self.camera_matrix[1, 1]

    def set_cx(self, cx):
        self.camera_matrix[0, 2] = cx

    def get_cx(self):
        return self.camera_matrix[0, 2]

    def set_cy(self, cy):
        self.camera_matrix[1, 2] = cy

    def get_cy(self):
        return self.camera_matrix[1, 2]
