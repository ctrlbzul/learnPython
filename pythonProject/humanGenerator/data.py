# import random and datetime module
import random
import datetime

# HUMAN DATAS
# hairstyles (men and women)
men_hairstyles = ['Pompadour', 'Slicked Back', 'High Fade', 'Undercut', 'Spiky']
women_hairstyles = ['Pony Tail', 'Long Hair', 'Dyed', 'Short Blonde', 'Bun']
# head shapes
head_shapes = ['Heart', 'Inverted Triangle', 'Triangle', 'Diamond', 'Oval']
# body types
body_types = ['Inverted Triangle', 'Rhomboid', 'Rectangle', 'Triangle','Oval']
# countries
countries = ['Afghanistan', 'Indonesia', 'Uruguay', 'England', 'Oman']

# functions
# print line
def printLine():
	  return '-------------------------------------'

# get gender
def getGender(gender_param):
	gender_param.lower() # handle the input as male, m, female and f
	if gender_param == 'male' or 'm':
		return 'Male'
	else:
		return 'Female'

# get age
def getAge():
	# generate random ages in range of 6 to 60
	ages = random.randint(6, 60)
	return ages

# get hairstyle
def getHairStyle(gender_param):
	if gender_param == 'male' or 'm':
		return random.choice(men_hairstyles)
	else:
		return random.choice(women_hairstyles)

# get head shape
def getHeadShape():
	return random.choice(head_shapes)

# get body type
def getBodyType():
	return random.choice(body_types)

# get country
def getCountry():
	return random.choice(countries)

# get current time
now = datetime.datetime.now()
current_time = now.strftime('%d %B %Y')
def getCreatedTime():
	return current_time