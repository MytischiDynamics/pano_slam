import SE3
import numpy as np


class Camera :
    def __init__(self):
        self.camera_extrinsics = SE3.SE3()
        self.camera_intrinsics = CameraIntrinsics()

    def SetTranlation(self, t):
        self.camera_extrinsics.SetTranslation(t)

    def Translate(self, t):
        self.camera_extrinsics.AddTraslation(t)


class CameraIntrinsics :
    def __init__(self):
        self.camera_matrix = np.zeros((3,3))
        self.distortion_coeffs = np.zeros(8)
