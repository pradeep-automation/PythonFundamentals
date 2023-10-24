def find_duplicates(arr, n):

    duplicates = []
    for i in range(n):
        index = arr[i] % n
        arr[index] += n

    for i in range(n):
        if arr[i] // n > 1:
            duplicates.append(i)

    if not duplicates:
        return -1

    return sorted(duplicates)

# Example 1
N1 = 4
arr1 = [0, 3, 1, 2]
print(find_duplicates(arr1, N1))  # Output: -1

# Example 2
N2 = 5
arr2 = [2, 3, 1, 2, 3]
print(find_duplicates(arr2, N2))  # Output: [2, 3]
