import copy

# Example list for demonstrating copies
original_list = [1, 2, [3, 4], 5]

# Shallow Copy
shallow_copied_list = copy.copy(original_list)

# Deep Copy
deep_copied_list = copy.deepcopy(original_list)

# Modifying the nested list in the shallow copy
shallow_copied_list[2][1] = 100

# Modifying the nested list in the deep copy
deep_copied_list[2][0] = 200

# Printing the original list and copied lists
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)
print("Deep Copied List:", deep_copied_list)
