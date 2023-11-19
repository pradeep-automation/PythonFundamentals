ls = [1, 3, 4, 2, 10, 8, 7, 9, 6]

def sort_list(lst: list):

    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst)//2]
    middle = [x for x in lst if x == pivot]
    left = [x for x in lst if x < pivot]

    right = [x for x in lst if x > pivot]

    return sort_list(left) + middle + sort_list(right)


print(sort_list(ls))
