def fall_distance(t):
    """
    Calculates the falling distance of an object due to gravity vs time.

    Calc:
        t (float): Seconds that the object has been falling.

    Gives:
        float: Meters that object has fallen in a specific period of time.
    """
    g = 9.8
    d = 0.5 * g * t**2
    return d