import cv2 as cv
from rig import Rig

class FrameWindow:
    def __init__(self):
        self.frames_list = []

    def push_frames_pack(self, frames_pack):
        self.frames_list.append(frames_pack)

    def remove_frames_pack(self, idx):
        self.frames_list = self.frames_list[:idx] + self.frames_list[idx:]


#Pack of frames simultaneously obtained from camera rig
class FramesPack:
    def __init__(self, indicies):
        self.frames = {}
        for idx in indicies:
            self.frames[idx] = cv.Mat()
