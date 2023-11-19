# import logging
#
# logging.basicConfig(filename='example.log', level=logging.INFO)
#
# def logger(func):
#
#     def log_func(*args):
#         logging.info(f"Running {func.__name__} with arguments {args}")
#         print(func(*args))
#     return log_func
#
# @logger
# def add(x, y):
#     return x+y
#
# @logger
# def sub(x, y):
#     return x-y
#
#
# add(10, 15)
# sub(20, 10)
#
# # add_logger = logger(add)
# # sub_logger = logger(sub)
# #
# # add_logger(5, 3)
# # sub_logger(10, 10)


import logging

logging.basicConfig(filename='my_file.log', level=logging.INFO)

def logger(func):

    def log_info(*args):
        logging.info(f'Function {func.__name__} runs with the arguments {args}')
        print(func(*args))
    return log_info

@logger
def mul(a, b):
    return a*b
@logger
def sum(a, b):
    return a+b


mul(12, 4)
sum(10, 5)

logg = logging.basicConfig(filename="myf.log", )
