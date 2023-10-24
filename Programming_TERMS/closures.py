def outer_fuc(message):

    def inner_fuc(name):
        print(f'{message} {name}')
    
    return inner_fuc



my_func = outer_fuc("Hello")
your_func = outer_fuc("Bolo")
my_func('Pradeep')
your_func('Ramola')
