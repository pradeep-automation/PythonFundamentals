def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # Code to execute before actual function
        print("I execute before actual function")
        result = original_function(*args, **kwargs)
        print("I execute after actual function")
        # Code to execute after the original function
        return result
    return wrapper_function


@decorator_function
def decorated_function(stt1,stt2):
    return f'Hello I am decorated function,{stt1}, {stt2}'


# Calling decorated function
res = decorated_function("Pradeep", "Ramola")
print(res)

def func(*args, **kwargs):
    print(type(args), type(kwargs))

func()




