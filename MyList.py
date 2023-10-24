# Lists

# Cars = ["Nexon", "Harrier", "CITY", "Taigun"]

# print(Cars[1], Cars[0])
# Cars.sort()
# print(Cars)
# Cars.append("Safari")
# print(Cars)
# Cars.insert(2, "Alto")
# Cars[3] = "Elevate"
# print("@@@@@@@@@@@@@@@@@@@@@@@")
# print(Cars)
# Cars.remove(Cars[10])
# print(Cars.pop(4))
# Cars.remove("XXCC")
# print(Cars)
# print("@@@@@@@@@@@@@@@@@@@@@@@$$$$$$$$$")
#
# num_list1 = [1, 5, 8, 3, 7]
# num_list2 = [10, 25, 20, 14]
# num_list1.extend(num_list2)
# print(num_list1)
# print(num_list2.copy() == num_list2)
# num_list1.clear()
# print(num_list1)
# print(num_list2)
# copy_list = num_list1.copy()
# print(copy_list)
# copy_list.sort(reverse=True)
# print(copy_list)
# string = "pradeep"
# print("".join(reversed(string)))
# for item in reversed(copy_list):
#     print(item)
# print(num_list1[0:])
# print(num_list1[0:2])
# print(num_list1[:-1])

# sort_list = sorted(num_list1)
# print(num_list1)
# print(sort_list)
#
#
# print("_________________________________________________________")
# nums = [1, 4, 6, 15, 9]
# print(max(nums))
# print(min(nums))
# print(sum(nums))
# #
# courses = ['Physics', 'Chemistry', 'CompSci', 'History']
# print(courses.index('CompSci'))
# # print(courses.index('Art'))
# print('History' in courses)
# print('Art' in courses)
# courses_str = ','.join(courses)
# print(courses_str)
# new_courses = courses_str.split(',')
# print(new_courses)

# my_list = [1,10,5,3,10,15,10,20, 10, 35]
# my_list.append(2)
# print(my_list)
# my_list.insert(1,10)
# print(my_list)
# print(my_list.index(10, 9))
import copy

# my_dict = {1:"banana",2:"apple",3:{3:"pine",4:"random"}}
#
# cop_dict = copy.copy(my_dict)
# cop_dict[1] = "Unknown"
# cop_dict[3].update({5:"shallow"})
# print(my_dict)
# print(cop_dict)
# print(my_dict.get(5, "orange"))
# print(my_dict)

# import copy
#
# ls = [1,3,4,[20, 30]]
# deep_ls = copy.deepcopy(ls)
# deep_ls[1] = 100
# deep_ls[3][1] = 300
# print(ls)
# print(deep_ls)

