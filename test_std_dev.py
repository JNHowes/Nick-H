# Author: Nick Howes
# GitHub username: JNHowes
# Date:May 10, 2023
# Description: Person Name and Age
# STD Dev of all persons and their ages.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age


def std_dev(person_list):
    """
    Calculate the population standard deviation of the ages of a list of Person objects.

    Args:
        person_list (list): A list of Person objects.

    Returns:
        float: The population standard deviation of the ages, or None if the list is empty.
    """
    if len(person_list) == 0:
        return None

    age_sum = 0
    for person in person_list:
        age_sum += person.get_age()
    age_mean = age_sum / len(person_list)

    variance_sum = 0
    for person in person_list:
        variance_sum += (person.get_age() - age_mean) ** 2
    variance = variance_sum / len(person_list)

    std_deviation = variance ** 0.5

    return std_deviation

