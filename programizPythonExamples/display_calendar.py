# Program to display calendar of the given month and year

# importing calendar module
import calendar

y = 2014 # year
m = 11 # month

# uncomment to take month and year input from the user
# y = int(input('Enter a year\t: '))
# m = int(input('Enter a month\t: '))

# display the calendar
print(calendar.month(y, m))
