import numpy as np
#import rig
import camera
import SE3

'''
def InitializeRig():
    camera_rig = rig.Rig()
    cam1 = camera.Camera()
    cam1.SetTranslation(np.array([1.0, 0.0, 0.0]))
    camera_rig.AddCamera(cam1)

    return camera_rig
'''

if __name__ == "__main__" :
    print("Testing Panorama SLAM")
    transform = SE3.SO3()
    transform.init_with_axis_angle(0.1, np.array([1.0, 1.0, 1.0]))
    new_p = transform.apply_to_point(np.array([1.0, 1.0, 0.0]))
    print(str(new_p))
