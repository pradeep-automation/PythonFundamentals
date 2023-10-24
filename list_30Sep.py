

def calculate(*args):
    if len(args) == 1:
        return "One argument"
    elif len(args)== 2:
        return "two argument"
    else:
        return "More arguments"


print(calculate(5))
print(calculate(1,3))
print(calculate(2, 3, 10, 5555))

