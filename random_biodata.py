import random as rd
import datetime as dt
import os

# clear console
os.system('clear')

print('/ RANDOM BIODATA /')

# generate random day, month, year
random_day = rd.randint(1, 31)
random_month = rd.randint(1,12)
random_year = rd.randint(1999, 2005)

# generate date of birth
date_of_birth = dt.date(random_year, random_month, random_day)
# function to get age
def get_age(born):
	today = dt.date.today()
	return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

# data list
names = ['Zill', 'Arthur', 'Aleister', 'Skud', 'Ormarr']
lives = ['California', 'Utah', 'Arizona', 'Wisconsin', 'Florida']
random_date = [random_day, random_month, random_year]

# print / generate random biodata
print('Hi, My name is', rd.choice(names))
print('I live in', rd.choice(lives))
print('Was born on ', end='') # end='' : to print in same line
print(*random_date, sep='-')
print('I am', get_age(date_of_birth), 'years old')

