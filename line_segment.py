# Author: Nick Howes
# GitHub username: JNHowes
# Date:May 31, 2023
# Description: Defines a Point class that has two data members, _x_coord and _y_coord, representing the two coordinates
# of the point.

import math

class Point:
    def __init__(self, x_coord, y_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        return self._x_coord

    def get_y_coord(self):
        return self._y_coord

    def distance_to(self, other_point):
        x1 = self._x_coord
        y1 = self._y_coord
        x2 = other_point.get_x_coord()
        y2 = other_point.get_y_coord()
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


class LineSegment:
    def __init__(self, endpoint_1, endpoint_2):
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = endpoint_2

    def get_endpoint_1(self):
        return self._endpoint_1

    def get_endpoint_2(self):
        return self._endpoint_2

    def length(self):
        return self._endpoint_1.distance_to(self._endpoint_2)

    def slope(self):
        x1 = self._endpoint_1.get_x_coord()
        y1 = self._endpoint_1.get_y_coord()
        x2 = self._endpoint_2.get_x_coord()
        y2 = self._endpoint_2.get_y_coord()
        if x2 - x1 == 0:  # Avoid division by zero
            return float('inf')
        return (y2 - y1) / (x2 - x1)

    def is_parallel_to(self, other_line_segment):
        return abs(self.slope() - other_line_segment.slope()) < 0.000001
