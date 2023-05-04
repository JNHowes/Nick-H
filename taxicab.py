def __init__(self, x_coord, y_coord):
    """Initialize the taxicab object with the given x and y coordinates, and initialize odometer to zero."""
    self._x_coord = x_coord
    self._y_coord = y_coord
    self._odometer = 0


def get_x_coord(self):
    """Return the current x-coordinate of the taxicab."""
    return self._x_coord


def get_y_coord(self):
    """Return the current y-coordinate of the taxicab."""
    return self._y_coord


def get_odometer(self):
    """Return the current odometer reading of the taxicab."""
    return self._odometer


def move_x(self, distance):
    """Move the taxicab by the given distance along the x-axis (positive for right, negative for left)."""
    self._x_coord += distance
    self._odometer += abs(distance)


def move_y(self, distance):
    """Move the taxicab by the given distance along the y-axis (positive for up, negative for down)."""
    self._y_coord += distance
    self._odometer += abs(distance)

