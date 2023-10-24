class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = f'{self.first}.{self.last}@testing.com'

    @property
    def email(self):
        return f'{self.first}.{self.last}@testing.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleted the name!!!')
        self.first = None
        self.last = None


emp1 = Employee('Pradeep', 'Ramola')

emp1.fullname = 'Sheldon Cooper'


print('-------->', emp1.first)
print('-------->', emp1.last)
print('-------->', emp1.email)
print('-------->', emp1.fullname)

del emp1.fullname

print('-------->', emp1.first)
print('-------->', emp1.last)
print('-------->', emp1.email)
print('-------->', emp1.fullname)

