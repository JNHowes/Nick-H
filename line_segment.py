# Author: Nick Howes
# GitHub username: JNHowes
# Date:May 31, 2023
# Description: Defines a Point class that has two data members, _x_coord and _y_coord, representing the two coordinates
# of the point.

import math

# Point class representing a point with x and y coordinates
class Point:
    """
    Initialize a Point object with x and y coordinates.

    Args:
        x_coord (float): The x-coordinate of the point.
        y_coord (float): The y-coordinate of the point.
    """

    def __init__(self, x_coord, y_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        """
        Get the x-coordinate of the point.

        Returns:
            float: The x-coordinate of the point.
        """
        return self._x_coord

    def get_y_coord(self):
        """
        Get the y-coordinate of the point.

        Returns:
            float: The y-coordinate of the point.
        """
        return self._y_coord

    def distance_to(self, other_point):
        """
        Calculate the distance between the current point and another point.

        Args:
            other_point (Point): The other point to calculate the distance to.

        Returns:
            float: The distance between the two points.
        """
        x1 = self._x_coord
        y1 = self._y_coord
        x2 = other_point.get_x_coord()
        y2 = other_point.get_y_coord()
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# LineSegment class representing a line segment between two points
class LineSegment:
    """
    Initialize a LineSegment object with two endpoints.

    Args:
        endpoint_1 (Point): The first endpoint of the line segment.
        endpoint_2 (Point): The second endpoint of the line segment.
    """

    def __init__(self, endpoint_1, endpoint_2):
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = endpoint_2

    def get_endpoint_1(self):
        """
        Get the first endpoint of the line segment.

        Returns:
            Point: The first endpoint of the line segment.
        """
        return self._endpoint_1

    def get_endpoint_2(self):
        """
        Get the second endpoint of the line segment.

        Returns:
            Point: The second endpoint of the line segment.
        """
        return self._endpoint_2

    def length(self):
        """
        Calculate the length of the line segment.

        Returns:
            float: The length of the line segment.
        """
        return self._endpoint_1.distance_to(self._endpoint_2)

    def slope(self):
        """
        Calculate the slope of the line segment.

        Returns:
            float or None: The slope of the line segment, or None if the line segment is vertical.
        """
        x1 = self._endpoint_1.get_x_coord()
        y1 = self._endpoint_1.get_y_coord()
        x2 = self._endpoint_2.get_x_coord()
        y2 = self._endpoint_2.get_y_coord()
        if x2 - x1 == 0:  # Avoid division by zero for vertical line segments
            return None
        return (y2 - y1) / (x2 - x1)

    def is_parallel_to(self, other_line_segment):
        """
        Check if the line segment is parallel to another line segment.

        Args:
            other_line_segment (LineSegment): The other line segment to compare with.

        Returns:
            bool: True if the line segments are parallel, False otherwise.
        """
        if self.length() == 0 or other_line_segment.length() == 0:
            return False
        return abs(self.slope() - other_line_segment.slope()) < 0.000001
