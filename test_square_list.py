# Author: Nick Howes
# GitHub username: JNHowes
# Date:May 17, 2023
# Description:Takes as a parameter a list of numbers and replaces each value with the square of that value.

def square_list(numbers):
    """Replace each value in the list with its square."""
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2
