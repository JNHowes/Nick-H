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
    if not person_list:
        return None

    # calculate the mean
    n = len(person_list)
    age_sum = sum([p.get_age() for p in person_list])
    mean = age_sum / n

    # calculate the sum of squares of deviations from the mean
    deviations_sum = sum([(p.get_age() - mean) ** 2 for p in person_list])

    # calculate the variance and standard deviation
    variance = deviations_sum / n
    std_dev = variance ** 0.5

    return std_dev
