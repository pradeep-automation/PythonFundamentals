
def open_file():
    f = open("testfile.txt")
    print(f.read())
    # name = bad_var
    # # raise AssertionError


try:
    open_file()
except FileNotFoundError as fe:
    print(fe)
# except NameError as ne:
#     print(ne)
else:
    print("I run if try block doesn't throw any exception!")
finally:
    print("I always run")
