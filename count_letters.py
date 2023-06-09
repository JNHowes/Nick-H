# Author: Nick Howes
# GitHub username: JNHowes
# Date:May 24, 2023
# Description: A function named count_letters that takes as a parameter a string and returns a dictionary
# that tabulates how many of each letter is in that string.

def count_letters(string):
    """
    Count the occurrences of each letter in a string and return a dictionary.

    Args:
        string (str): The input string.

    Returns:
        dict: A dictionary with uppercase letters as keys and their counts as values.
    """
    letter_counts = {}
    for char in string:
        if char.isalpha():
            char = char.upper()
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts
