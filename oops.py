""" Python Object-Oriented Programming """


class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + '.' + last + '@testing.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def __repr__(self):
        return f'Employee({self.first}, {self.last})'

    def __str__(self):
        return f'----> {self.fullname()} ---- {self.email}'

    def __add__(self, other):
        return self.salary + other.salary




emp_1 = Employee('Pradeep', 'Ramola', 50000)
emp_2 = Employee('Akanksha', 'Rana', 60000)
#
# emp_1.first = 'Pradeep'
# emp_1.last = 'Ramola'
# emp_1.email = 'pradeep.ramola@testing.com'
# emp_1.salary = 50000
#
#
# emp_2.first = 'Akanksha'
# emp_2.last = 'Rana'
# emp_2.email = 'akanksha.rana@testing.com'
# emp_2.salary = 60000

print(emp_1.email)
print(emp_2.email)
print(emp_2.fullname())
# print(Employee.fullname(emp_1))

print(emp_1)



print(1+2)
print(int.__add__(1, 2))

# print(emp_1.__add__(emp_2))
print(emp_1+emp_2)





