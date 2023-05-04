def multiply(a, b):
    """
    Return the product of two positive integers using recursion and addition.

    Parameters:
    a (integer): The first positive integer to be multiplied.
    b (integer): The second positive integer to be multiplied.

    Returns:
    integer: The product of a and b.
    """
    if a == 1:
        return b
    elif b == 1:
        return a
    else:
        return a + multiply(a, b - 1)
