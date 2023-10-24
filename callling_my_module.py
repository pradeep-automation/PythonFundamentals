# import my_module as mm
import random
import calendar

from my_module import *
import sys
import datetime
from my_module import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']
# print(find_index(courses, 'Art'))
# print(test)

print(sys.path)


random_course = random.choice(courses)
print(random_course)
print(calendar.isleap(1900))
import antigravity
