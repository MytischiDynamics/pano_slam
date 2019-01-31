import numpy as np
import rig
import camera


def InitializeRig():
    camera_rig = rig.Rig()
    cam1 = camera.Camera()
    cam1.SetTranslation(np.array([1.0, 0.0, 0.0]))
    camera_rig.AddCamera(cam1)

    return camera_rig


if __name__ == "__main__" :
    print("Testing Panorama SLAM")
