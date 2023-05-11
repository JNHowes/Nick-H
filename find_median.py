# Author: Nick Howes
# GitHub username: JNHowes
# Date:May 10, 2023
# Description: Find Median
# Find's statistical median of a list of numbers.

def find_median(numbers):
    """
    Return the statistical median of a list of numbers.
    """
    if not numbers:
        return None

    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    midpoint = length // 2

    if length % 2 == 0:
        return (sorted_numbers[midpoint - 1] + sorted_numbers[midpoint]) / 2
    else:
        return sorted_numbers[midpoint]