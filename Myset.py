# Sets are unordered and duplicates are not allowed

cs_courses = {'History', 'Science', 'English', 'Art'}
art_courses = {'History', 'Science', 'Math', 'Design'}
print(cs_courses)
print('History' in cs_courses)
# cs_courses.discard("History")
# cs_courses.clear()
# cs_courses.symmetric_difference_update(art_courses)
print(cs_courses)

#
# print(cs_courses.intersection(art_courses))
#
# print(cs_courses.difference(art_courses))
# print(cs_courses.union(art_courses))
#
# print('------------------------------------------------------')
#
# # Empty lists
# empty_list = []
# empty_list2 = list()
# print(type(empty_list))
# print(type(empty_list2))
# # Empty tuples
# empty_tuple = ()
# empty_tuple2 = tuple()
# print(type(empty_tuple))
# print(type(empty_tuple2))
#
# # Empty set
# empty_set = {}    # This is not set. It's a dictionary
# empty_set2 = set()
# print(type(empty_set))
# print(type(empty_set2))
