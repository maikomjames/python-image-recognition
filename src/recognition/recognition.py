
import cv2
import numpy as np
from matplotlib import pyplot as plt


class Recognition:

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

        self.points = []
        self.dimensions = ()

    def find(self, img):

        img_rgb = cv2.imread(self.image)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(img, 0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        self.set_points(max_loc, (w, h))

        return [max_loc, (max_loc[0] + w, max_loc[1] + h)]

    def get_dimensions(self):
        return self.dimensions

    def set_points(self, loc, size):

        w, h = size
        x, y = loc
        self.dimensions = size

        """ top left """
        self.points.append(loc)
        """ center left """
        self.points.append((x, y + h/2))
        """ bottom left """
        self.points.append((x, y + h))
        """ top center """
        self.points.append((x + w/2, y))
        """ center """
        self.points.append((x + w/2, y + h/2))
        """ bottom center """
        self.points.append((x + w / 2, y + h))
        """ top right """
        self.points.append((x + w, y))
        """ center right"""
        self.points.append((x + w, y + h/2))
        """ bottom right"""
        self.points.append((x + w, y + h))

    def get_top_left(self):
        return self.points[0]

    def get_center_left(self):
        return self.points[1]

    def get_bottom_left(self):
        return self.points[2]

    def get_top_center(self):
        return self.points[3]

    def get_center(self):
        return self.points[4]

    def get_bottom_center(self):
        return self.points[5]

    def get_top_right(self):
        return self.points[6]

    def get_center_right(self):
        return self.points[7]

    def get_bottom_right(self):
        return self.points[8]
