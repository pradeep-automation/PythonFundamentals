month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month: int):
    if not 1 <= month <= 12:
        return "Invalid Month"
    if month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 29
    return month_days[month]


print(days_in_month(1900, 2))

import calendar

print(calendar.isleap(2024))

