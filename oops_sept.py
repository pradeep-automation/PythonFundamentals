import datetime
class Employee:
    num_of_emps = 0
    __raise_amt = 1.4

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last +'@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    @property
    def raise_amt_func(self):
        return self.__raise_amt

    @raise_amt_func.setter
    def raise_amt_func(self, amount):
        self.__raise_amt = amount

    def fullname(self):
        return self.first + " " + self.last

    def apply_raise(self):
        self.pay = int(int(self.pay) * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workingday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __str__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"


my_date = datetime.date(2023, 9, 16)
print(Employee.is_workingday(my_date))

print(Employee.num_of_emps)
emp1 = Employee("Pradeep", "Ramola", 1000)
print(emp1.fullname())
print(emp1.raise_amt_func)
Employee.set_raise_amt(1.5)
emp1.apply_raise()
print(emp1.pay)
print(Employee.num_of_emps)

emp2 = "king-Singh-70000"
emp3 = "kig-Singh-80000"
# first, last, pay = emp2.split("-")
# new_emp = Employee(first, last, pay)
new_emp1 = Employee.from_string(emp2)
new_emp2 = Employee.from_string(emp3)
new_emp2.apply_raise()
print(new_emp2.pay)
print(Employee.num_of_emps)
