import SE3
import camera

class Rig:
    def __init__(self):
        self.cameras = {}
        self.stereo_cameras = {}
        self.max_camera_idx = 0
        self.max_stereo_camera_idx = 0
        self.transform = SE3.SE3()

    def AddCamera(self, camera_struct):
        self.camereas[self.max_camera_idx] = camera_struct
        self.max_camera_idx += 1

    def GenerateCameraInGlobalCoords(self, camera_idx):
        cur_cam = self.cameras[camera_idx]
        rig_transform = self.transform
        camera_local_transform = cur_cam.GetTransform()


#    def ProjectPoint(self, camera_idx, p):
