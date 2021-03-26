# import modules
import calendar
from datetime import datetime

# function to print a straight line
def printLine():
	print('----------------------------------------')

# get current date and time
now = datetime.now()
today = int(now.strftime("%d"))
now_month = int(now.strftime("%m"))
now_year = int(now.strftime("%Y"))

# function to count the age
def count_age(day_input, month_input, year_input): 
  if day_input == today and month_input == now_month:
    your_age = now_year - year_input
    print(your_age)
    print('WOW TODAY IS YOUR BIRTHDAY!!')
  elif day_input < today and month_input <= now_month :
    your_age = now_year - year_input
    print("You are ", your_age, "year old.")
    print('YOUR BIRTHDAY HAS PASSED.')
  else:
    your_age = now_year - year_input - 1
    print("YOU ARE", your_age, "YEARS OLD.")

day = int(input("Input your birth day (1-31): "))
month = int(input("Input your birth month (1-12) : "))
year = int(input("Input your birth year : "))

# get month name by given integer (month)
monthName = calendar.month_name[month]

# print the output
printLine()
print(now.strftime('TODAY IS : %-d %B %Y'))
printLine()
print("YOUR BIRTHDAY\t: {0} {1} {2}".format(day, monthName, year))
count_age(day, month, year)
printLine()
