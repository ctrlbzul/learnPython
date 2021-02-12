import random as rd
import datetime as dt
import os

# clear console
os.system('clear')

# function to print straight line
def printLine():
  print('-----------------------------------')

# function to get age
def get_age(born):
	today = dt.date.today()
	return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

print('// RANDOM BIODATA //')
printLine()
# generate random day, month, year
random_day = rd.randint(1,31)
random_month = rd.randint(1,12)
random_year = rd.randint(1999, 2005)

# generate date of birth
# if condition to "solve" ValueError: day is out of range for month ehehe :v
if random_day > 28:
	random_month = rd.randint(3, 12)
date_of_birth = dt.date(random_year, random_month, random_day)

# data lists
names = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo']
lives = ['California', 'Utah', 'Arizona', 'Wisconsin', 'Florida']
random_date = [random_day, random_month, random_year]

# print (generate) random biodata
print('Hi, My name is {0}'.format(rd.choice(names)))
print('I live in {0}'.format(rd.choice(lives)))
print('Was born on ', end='') # end='' : to print in same line
print(*random_date, sep='-')
print('I am {0} years old'.format(get_age(date_of_birth)))
printLine()

