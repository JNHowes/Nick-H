# Author: Nick Howes
# GitHub username: JNHowes
# Date:May 24, 2023
# Description:

class Employee:
    def __init__(self, name, id_number, salary, email_address):
        self._name = name
        self._id_number = id_number
        self._salary = salary
        self._email_address = email_address

    def get_name(self):
        return self._name

    def get_id_number(self):
        return self._id_number

    def get_salary(self):
        return self._salary

    def get_email_address(self):
        return self._email_address


def make_employee_dict(names, ids, salaries, emails):
    employees = {}
    for name, id_number, salary, email in zip(names, ids, salaries, emails):
        employee = Employee(name, id_number, salary, email)
        employees[id_number] = employee
    return employees


# Example usage
names = ["Jean", "Kat", "Pomona"]
ids = ["100", "101", "102"]
salaries = [30, 35, 28]
emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
employees = make_employee_dict(names, ids, salaries, emails)

print(employees["100"].get_name())  # Output: Jean
