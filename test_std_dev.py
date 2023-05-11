# Author: Nick Howes
# GitHub username: JNHowes
# Date:May 10, 2023
# Description: Person Name and Age
# STD Dev of all persons and their ages.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age


def std_dev(person_list):
    if not person_list:
        return None

    n = len(person_list)
    ages = [person.get_age() for person in person_list]
    mean = sum(ages) / n
    variance = sum((age - mean) ** 2 for age in ages) / n
    std_dev = variance ** 0.5

    return std_dev


