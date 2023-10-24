class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + '.' + last + '@testing.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.salary = self.salary * self.raise_amt


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, salary, emp_list=None):
        super().__init__(first, last, salary)

        if emp_list is None:
            self.emp_list = []
        else:
            self.emp_list = emp_list

    def add_employee(self, emp):
        if emp not in self.emp_list:
            self.emp_list.append(emp)

    def delete_employee(self, emp):
        if emp in self.emp_list:
            self.emp_list.remove(emp)

    def print_emps(self):
        for emp in self.emp_list:
            print("--->", emp.fullname())


dev1 = Developer('Pradeep', 'Ramola', 2400000, 'Python')
dev2 = Developer('Eva', 'Rana', 2300000, 'Golang')
#
# dev1.apply_raise()
# print(dev1.salary)
# print(dev2.salary)
#
# print(dev1.prog_lang)

manager1 = Manager('Sue', 'Smith', 150000, [dev1])

print(manager1.emp_list)
manager1.add_employee(dev2)
manager1.delete_employee(dev1)
manager1.print_emps()


print(isinstance(manager1, Manager))
print(issubclass(Manager, Employee))




