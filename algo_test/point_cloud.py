import numpy as np


class Point:
    def __init__(self):
        self.coords = np.zeros(3)


class PointCloud:
    def __init__(self):
        self.points = {}
        self.max_point_idx = 0

    def AddPoint(self, p):
        self.points[self.max_point_idx] = p
        self.max_point_idx += 1
