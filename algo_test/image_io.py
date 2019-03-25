import cv2 as cv
from os import listdir
from os.path import isfile, join
from camera import Camera


class ImageReader:
    def __init__(self):
        self.num_images = 0
        self.all_images = 0
        self.folder_path = ""
        self.folder_list = []
        self.num_sources = 0

    def update_folder(self):
        contents = listdir(self.folder_path)
        for entry in contents:
            cur_path = join(self.folder_path, entry)
            if not isfile(cur_path):
                self.folder_list.append(cur_path)

    def set_folder(self, folder_path):
        self.folder_path = folder_path


class CalibrationReader:
    def __init__(self, calib_file):
        self.calibration_file = calib_file
        self.transform_list = {}

    def read_calibration(self):
