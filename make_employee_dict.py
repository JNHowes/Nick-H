# Author: Nick Howes
# GitHub username: JNHowes
# Date:May 24, 2023
# Description: A class named Employee that has private data members for an employee's _name, _ID_number, _salary,
# and _email_address.

class Employee:
    """Class representing an employee."""

    def __init__(self, name, id_number, salary, email_address):
        """
        Initialize the Employee object.

        Args:
            name (str): The name of the employee.
            id_number (str): The ID number of the employee.
            salary (float): The salary of the employee.
            email_address (str): The email address of the employee.
        """
        self._name = name
        self._id_number = id_number
        self._salary = salary
        self._email_address = email_address

    def get_name(self):
        """Return the name of the employee."""
        return self._name

    def get_id_number(self):
        """Return the ID number of the employee."""
        return self._id_number

    def get_salary(self):
        """Return the salary of the employee."""
        return self._salary

    def get_email_address(self):
        """Return the email address of the employee."""
        return self._email_address


def make_employee_dict(names, ids, salaries, emails):
    """
    Create a dictionary of Employee objects.

    Args:
        names (list): List of employee names.
        ids (list): List of employee ID numbers.
        salaries (list): List of employee salaries.
        emails (list): List of employee email addresses.

    Returns:
        dict: A dictionary where the key is the ID number and the value is the Employee object.
    """
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
