import numpy as np


class Point:
    def __init__(self):
        self.coords = np.transpose(np.zeros(3))

    def get_coords(self):
        return self.coords

    def set_coords(self, p):
        self.coords = p

    def get_homogeneous_coords(self):
        return np.vstack((self.coords, np.array([1.0])))

    def set_homogeneous_coords(self, p):
        self.coords = p[:-1]
        self.coords = self.coords / p[-1]

class PointCloud:
    def __init__(self):
        self.points = {}
        self.max_point_idx = 0

    def AddPoint(self, p):
        self.points[self.max_point_idx] = p
        self.max_point_idx += 1
