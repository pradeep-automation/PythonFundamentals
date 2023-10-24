def square(x):
    return x*x

def cube(x):
    return x*x*x

#
# f = square
#
# print(square(3))
# print(f(4))

def my_map(func, args_list):
    result = []
    for i in args_list:
        result.append(func(i))
    return result


squares = my_map(square, [1, 2, 3, 4])
print(squares)

cubes = my_map(cube, [1, 2, 3, 4])
print(cubes)



# def logger(msg):
#
#     def log_msg():
#         print("Log:", msg)
#     msg = "Hello"
#     return log_msg
#
#
# log_hi = logger("HIIII!!")
# log_hi()


def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')
    return wrap_text


print_h1 = html_tag("h1")
print_h1("I am headline1")

print_p = html_tag("p")
print_p("I am paragraph")


