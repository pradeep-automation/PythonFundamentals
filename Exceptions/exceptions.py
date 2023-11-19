#
# def open_file():
#     f = open("testfile.txt")
#     print(f.read())
#     # name = bad_var
#     # # raise AssertionError
#
#
# try:
#     open_file()
# except FileNotFoundError as fe:
#     print(fe)
# # except NameError as ne:
# #     print(ne)
# else:
#     print("I run if try block doesn't throw any exception!")
# finally:
#     print("I always run")
from Exceptions.my_exp import CustomEx


class Test:

    def zero_div(self, a, b):

        try:
            if b == 0:
                raise CustomEx
            res = a / b
            return res
        except CustomEx as z:
            print(z.msg)

test = Test()
result = test.zero_div(10, 0)
if result:
    print(f"result is {result}")


