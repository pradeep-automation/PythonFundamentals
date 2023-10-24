# def hello_func():
#     pass
#
# print(hello_func())
#
# def hello_func():
#     print("hello function!!!")
#
#
# hello_func()

# def hello_func():
#     return 'Hello Function!!!'
#
# print(hello_func().upper())

def hello_func(greetings, name= 'You'):
    return f'{greetings} {name} function'

print(hello_func('Hello', name='Pradeep'))

print('^^^^^^^^^^^^^^^^^^^^^^^^^^')

def student_info(*args, **kwargs):
    print((args))
    print((kwargs))

student_info()
student_info('Math', 'Art', name= 'Pradeep', age = '33')


# subject = ['Math', 'Art']
# info = {'name' : 'Pradeep', 'age' : '33'}
# student_info(subject, info)

