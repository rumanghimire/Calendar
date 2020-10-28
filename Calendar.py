# First, we need to import a calendar module.

import calendar
print(calendar.weekheader(1))
# Here, you will be able to see the first alphabet of each week days. Output will be: M T W T F S S

# If you put 2 in the tuples of weekheader you will be able to see first two alphabet of week days.
print(calendar.weekheader(2))
# Output : Mo Tu We Th Fr Sa Su

# To print calendar of entire year.
print(calendar.calendar(2020))
# Output: 2020
#
#       January                   February                   March
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#        1  2  3  4  5                      1  2                         1
#  6  7  8  9 10 11 12       3  4  5  6  7  8  9       2  3  4  5  6  7  8
# 13 14 15 16 17 18 19      10 11 12 13 14 15 16       9 10 11 12 13 14 15
# 20 21 22 23 24 25 26      17 18 19 20 21 22 23      16 17 18 19 20 21 22
# 27 28 29 30 31            24 25 26 27 28 29         23 24 25 26 27 28 29
#                                                     30 31
#
#        April                      May                       June
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#        1  2  3  4  5                   1  2  3       1  2  3  4  5  6  7
#  6  7  8  9 10 11 12       4  5  6  7  8  9 10       8  9 10 11 12 13 14
# 13 14 15 16 17 18 19      11 12 13 14 15 16 17      15 16 17 18 19 20 21
# 20 21 22 23 24 25 26      18 19 20 21 22 23 24      22 23 24 25 26 27 28
# 27 28 29 30               25 26 27 28 29 30 31      29 30
#
#         July                     August                  September
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#        1  2  3  4  5                      1  2          1  2  3  4  5  6
#  6  7  8  9 10 11 12       3  4  5  6  7  8  9       7  8  9 10 11 12 13
# 13 14 15 16 17 18 19      10 11 12 13 14 15 16      14 15 16 17 18 19 20
# 20 21 22 23 24 25 26      17 18 19 20 21 22 23      21 22 23 24 25 26 27
# 27 28 29 30 31            24 25 26 27 28 29 30      28 29 30
#                           31
#
#       October                   November                  December
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#           1  2  3  4                         1          1  2  3  4  5  6
#  5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13
# 12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20
# 19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27
# 26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31
#                           30

# To print the calendar of particular year and month.
print(calendar.month(2020, 8))
# Here you will be able to see calendar of August, 2020.
# Output:  August 2020
# Mo Tu We Th Fr Sa Su
#                 1  2
#  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30
# 31


# To find a weekday with given year, month and day-date.
day_of_the_week = calendar.weekday(2020, 10, 28)
print(day_of_the_week)
# Output will be 2, which means Wednesday.
# 0= monday, 1 = Tuesday, 2= Wednesday, 3 =Thursday, 4= Friday, 5 =Saturday, 6 =Sunday


# To know whether a year is leap year or not
leap_year = calendar.isleap(2020)
print(leap_year)
# If the input year is leap year, result will be True elseif False.


