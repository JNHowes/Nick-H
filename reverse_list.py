# Author: Nick Howes
# GitHub username: JNHowes
# Date:May 17, 2023
# Description: Takes as a parameter a list and reverses the order of the elements in that list.

def reverse_list(lst):
    """
    Mutates the original list by reversing the order of its elements.
    """
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
