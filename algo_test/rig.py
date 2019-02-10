import SE3
import camera


class Rig:
    def __init__(self):
        self.cameras = {}
        self.stereo_cameras = {}
#       self.max_camera_idx = 0
#       self.max_stereo_camera_idx = 0
        self.transform = SE3.SE3()

    def add_camera(self, camera_struct, idx):
        self.camereas[idx] = camera_struct
#       self.max_camera_idx += 1

    def generate_camera_in_global_coords(self, camera_idx):
        cur_cam = self.cameras[camera_idx]
        rig_transform = self.transform
        camera_local_transform = cur_cam.get_transform()

#       TODO! Check multiplication sequence
        cur_cam.set_transform(rig_transform * camera_local_transform)
        return cur_cam

    def project_point_to_camera(self, camera_idx):
        cur_cam = self.generate_camera_in_global_coords(camera_idx)

    def get_indicies_list(self):
        return list(self.cameras.keys())
