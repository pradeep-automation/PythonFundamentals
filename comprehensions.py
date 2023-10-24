nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n' for each 'n' in nums

my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)
my_list = [n for n in nums]
print(my_list)

# I want 'n*n' for each 'n' in nums
# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)
# my_list = [n*n for n in nums]
# print(my_list)

# I want 'n' for each 'n' in num if n is even.
# my_list = []
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
# print(my_list)
# my_list = [n for n in nums if n%2 == 0]
# print(my_list)


'''I want a (letter, num) pair for each letter in abcd and each number in 1234'''
# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)


