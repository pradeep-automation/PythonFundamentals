
ls = [x for x in range(21) if x % 2 == 0]
print(ls)



def my_map(func):
    result = []
    ls = [2, 3, 5]
    def inner_func(*args):
        for i in ls:
            result.append(func(i))
        return result
    return inner_func

@my_map
def square(x):
    return x*x


print(square(3))

# def cube(x):
#     return x*x*x
#
#
# print(my_map(cube, [1, 2, 3]))
