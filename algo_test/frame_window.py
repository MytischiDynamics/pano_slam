import cv2 as cv
from camera import Camera
from rig import Rig

class FrameWindow:
    def __init__(self):
        self.frames_queue = []

    def push_frames_pack(self, frames_pack):
        self.frames_queue.append(frames_pack)

    def remove_frames_pack(self, idx):
        self.frames_queue = self.frames_queue[:idx] + self.frames_queue[idx:]


#Pack of frames simultaneously obtained from camera rig
class FramesPack:
    def __init__(self, indicies):
        self.frames = {}
        for idx in indicies:
            self.frames[idx] = Frame()


class Frame:
    def __init__(self, pic):
        self.image = pic
        self.camera = Camera()

    def __init__(self):
        self.image = cv.Mat()
