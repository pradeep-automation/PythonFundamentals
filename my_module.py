print('Imported my module...')

test = 'Test String'

def find_index(to_search, target):
    '''find the index of a value in a sequence'''
    for index, value in enumerate(to_search):
        if value == target:
            return index
    return -1

