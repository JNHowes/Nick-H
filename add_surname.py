# Author: Nick Howes
# GitHub username: JNHowes
# Date:May 10, 2023
# Description: Add surname Kardashian to K first names.
# Adds Surname Kardashian if first name starts with K.

def add_surname(names):
    """
    Returns a list of first names that start with "K", with the surname "Kardashian" added to each one, with a space
    between the first and last names.

    :param names: A list of first names
    :return: A list of first names that start with a "K", with the surname "Kardashian" added to each one
    """
    return [name + " Kardashian" for name in names if name.startswith("K")]
