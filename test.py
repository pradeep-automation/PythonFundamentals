class Employee:

    raise_amt = 1.3
    num_of_emp = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = float(salary)
        self.email = f"{self.fname}.{self.lname}@test.com"

        Employee.num_of_emp += 1

    def fullname(self):
        return f"{self.fname} {self.lname}"


    def raise_salary(self):
        self.salary = self.salary * Employee.raise_amt


print(Employee.num_of_emp)
emp1 = Employee('Pradeep', 'Ramola', 10000)
print(Employee.num_of_emp)
emp2 = Employee("Sam", "Pitroda", 25000)
print(emp2.salary)
emp1.raise_salary()
print(emp1.email)
print(emp1.salary)
print(emp1.fullname())
emp2.raise_salary()
print(emp2.salary)
print(Employee.num_of_emp)

    