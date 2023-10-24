# Class variables are shared among all the instances of the class

class Employee:

    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay=0):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@testing.com'

        Employee.num_of_emp += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        # self.pay = (self.pay * Employee.raise_amount)
        self.pay = (self.pay * self.raise_amount)

# print(Employee.__dict__)
print(Employee.num_of_emp)
emp1 = Employee('Marlon', 'Brando', 80000)
emp2 = Employee('Al', 'Pacino', 70000)
#
# print(emp1.first)
# print(emp1.fullname())
# print(emp1.email)
# print(emp1.pay)
# emp1.apply_raise()
# Employee.raise_amount = 1.05
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# emp1.raise_amount = 1.03
#
# print(emp1.raise_amount)
# print(emp2.raise_amount)

print(Employee.num_of_emp)




