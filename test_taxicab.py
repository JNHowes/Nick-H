# Author: Nick Howes
# GitHub username: JNHowes
# Date:May 3, 2023
# Description: Taxicab with three private data members:
# 1. Current X coordinate, 2. Current Y coordinate, 3. Current Odometer.

class Taxicab:
    """
    A class that represents a taxicab with current x-coordinate, y-coordinate, and odometer reading.
    """

    def __init__(self, x_coord, y_coord):
        """
        Initializes the taxicab's x-coordinate, y-coordinate, and odometer reading.

        Parameters:
        x_coord (int): The initial x-coordinate.
        y_coord (int): The initial y-coordinate.
        """
        self.__x_coord = x_coord
        self.__y_coord = y_coord
        self.__odometer = 0

    def get_x_coord(self):
        """
        Returns the current x-coordinate of the taxicab.

        Returns:
        int: The current x-coordinate.
        """
        return self.__x_coord

    def get_y_coord(self):
        """
        Returns the current y-coordinate of the taxicab.

        Returns:
        int: The current y-coordinate.
        """
        return self.__y_coord

    def get_odometer(self):
        """
        Returns the current odometer reading of the taxicab.

        Returns:
        int: The current odometer reading.
        """
        return self.__odometer

    def move_x(self, distance):
        """
        Moves the taxicab left or right by a given distance.

        Parameters:
        distance (int): The distance to move the taxicab. Positive values move the taxicab right,
                        while negative values move the taxicab left.
        """
        self.__x_coord += distance
        self.__odometer += abs(distance)

    def move_y(self, distance):
        """
        Moves the taxicab up or down by a given distance.

        Parameters:
        distance (int): The distance to move the taxicab. Positive values move the taxicab up,
                        while negative values move the taxicab down.
        """
        self.__y_coord += distance
        self.__odometer += abs(distance)

