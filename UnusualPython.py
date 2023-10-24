def unusual_func(x:list):
    if all(x):
        return "Hello"
    elif not x:
        return "HI"
    else:
        return "GoodBYE!!!!"


lst = [1, 2, -3, 5, 0]
lst1 = [1, 1]
print(unusual_func(lst))
