import sys
import slam_system

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
    if len(sys.argv != 3) :
        print("Usage: " + sys.argv[0] + " dataset_folder calibration_file")
        exit(0)
    camera_file = sys.argv[2]
    dataset_folder = sys.argv[1]

    pano_slam = slam_system()