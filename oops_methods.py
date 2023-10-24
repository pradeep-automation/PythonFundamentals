class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + '.' + last + '@testing.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # Alternative constructor method
    @classmethod
    def from_string(cls, emp_str):
        first, last, salary = emp_str.split('-')
        return cls(first, last, salary)

    @staticmethod
    def is_workday(day):
        if day.weekday() in [5,6]:
            return False
        return True

emp1 = Employee('Marlon', 'Brando', 80000)
emp2 = Employee('Al', 'Pacino', 70000)


# Alternative constructor Implementation
emp_str_1 = 'John-Doe-75000'
emp_str_2 = 'Sam-Dey-85000'
emp_str_3 = 'Bear-Khan-100000'

# first, last, salary = emp_str_1.split('-')

# new_emp1 = Employee(first, last, salary)

new_emp1 = Employee.from_string(emp_str_1)

print(new_emp1.first)
print(new_emp1.salary)


import datetime
my_date = datetime.date(2023, 7, 14)
print(Employee.is_workday(my_date))









# Employee.set_raise_amt(1.7)
#
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)


# print(emp1.set_raise_amt())




    

