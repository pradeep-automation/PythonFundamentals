import copy

coordinates = (10,20)
x, y = coordinates   # Unpacking tuples

#print(x)
#print("y is", y)
# first_name = ['Eva', 'Akanksha', 'Paapu']
# last_name = 'Ramola'
# for f_name in first_name:
#     print (f'{f_name} {last_name}') */
print('#######################################################################')
# Lists are mutable
courses = ['History', 'Art', 'CompSci', 'English']
new_courses = courses
courses.append('Maths')
courses[0] = 'Civics'
print(courses)
print(new_courses)

# Tuples are immutable
courses_tuple = ('History', 'Art', 'CompSci', 'English')
new_courses_tuple = courses_tuple
print(courses_tuple)
print(new_courses_tuple[0])
# courses_tuple[0] = 'Civics' #Not allowed








