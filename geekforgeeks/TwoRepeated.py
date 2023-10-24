def twoRepeated(arr, n):
    res = []
    first = False

    # iterating over the array elements.
    for i in range(0, n + 2):

        # making the visited elements negative.
        if arr[abs(arr[i])] > 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]

        # if the number is negative, it was visited previously
        # so this would be the repeated element.
        else:

            # storing first and second repeated element accordingly.
            if first == False:
                res.append(abs(arr[i]))
                first = True
            else:
                res.append(abs(arr[i]))
                break

    # returning the result.
    return res


n = 5
my_list = [1, 5, 3, 4, 3, 1, 2]

print(twoRepeated(my_list, n))


