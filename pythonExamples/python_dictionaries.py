# PYTHON EXAMPLE : DICTIONARY

# funtion : show menu
def showMenu():
  print('''1. Create and print a dictionary\
  \n2. Access a dictionary item\
  \n3. Change a dictionary item\
  \n4. Print all dict keys (1 by 1)\
  \n5. Print all dict values (1 by 1)\
  \n6. Return values with values() function\
	\n7. Loop through both keys and values with items() function\
	\n8. Check if a key exist in a dictionary\
	\n9. Get the length of a dictionary\
	\n10. Add, remove and empty a dictionary\
	\n11. create a dictionary with the dict() constructor''')

# function : print a straight line
def printLine():
  print('------------------------------------------------------------')

# function : create and print a dictionary (1)
def createAndPrintDict():
	# create a dictonary
	global car # make car as a global variable
	car = {
		"brand" : "Ford",
		"model" : "Mustang",
		"year" : "1964"
		}
	# print the dictionary (dict)
	return(f'>> {car}')

# function : access the car dict item (2)
def accessTheItem():
	# access the items
	item = car["model"]
	return(f'>> {item}')

# function : change dict item (3)
def changeDictItem():
	# change the value of a spesific item
	car["year"] = '2021' # year : 1964 >> 2021
	return(f'>> {car}')

# function : print all dict keys (1 by 1) (4)
def printDictKeys():
	# print all key names, 1 by 1
	print('KEYS :')
	for key in car:
		print(f'>> {key}')

# function : print all dict values (1 by 1) (5)
def printDictValues():
	# print all values, 1 by 1
	print('VALUES :')
	for value in car:
		print(f'>> {car[value]}')

# function : return values with values() function (6)
def returnValues():
	print('VALUES WITH values() FUNCTION :')
	for value in car.values():
		print(f'>> {value}')

# function : loop through both keys and values, using items() function (7)
def loopKeysAndValues():
	print('VALUES WITH items() FUNCTION :')
	for key, value in car.items():
		print(f'>> {key, value}')

# function : check if a key exist (8)
def isKeyExist():
	if "year" in car:
		print('>> Yes, [year] is one of the keys in the car dictionary')
	else:
		print('>> Key does not exits')

# function : get the length of a dict (9)
def dictLength():
	return len(car)

# function : add, remove and empty a dictionary (10)
def addRemoveEmptyDict():
	print(f'car dict : {car}')
	# add item to dict
	car["color"] = "red"
	print(f'>> Item added : {car}')
	# remove an item from a dict
	car.pop("year")
	print(f'>> Item removed : {car}')
	# empty a dictionary
	car.clear()
	print(f'>> Dict emptied : {car}')

# create a dictionary with the dict() constructor (11)
def createNewDict():
	print('Dict created : new car')
	new_car = dict(brand = "Ferrari", color = "orange", year = "2019")
	print(f'>> New car : {new_car}')

# MAIN DISPLAY
print('// PYTHON EXAMPLE : DICTIONARY //')
printLine()
showMenu()

# get user input (str)
printLine()
menu = input('Choose the menu (1-11) : ')
printLine()

# handling menu input
if menu == '1':
  print('>> 1. Create and print a dictionary')
  print(f'{createAndPrintDict()}')
elif menu == '2':
  print('>> 2. Access a dictionary item')
  print(f'{accessTheItem()}')
elif menu == '3':
  print('>> 3. Change a dictionary item')
  print(f'{changeDictItem()}')
elif menu == '4':
  print('>> 4. Print all dict keys (1 by 1)')
  print(f'{printDictKeys()}')
elif menu == '5':
  print('>> 4. Print all dict values (1 by 1)')
  print(f'{printDictValues()}')
elif menu == '6':
  print('>> 6. Return values with values() function')
  print(f'{returnValues()}')
elif menu == '7':
	print('7. Loop through both keys and values with items() function')
	print(f'{loopKeysAndValues()}')
elif menu == '8':
	print('8. Check if a key exist in a dictionary')
	print(f'{isKeyExist()}')
elif menu == '9':
	print('9. Get the length of a dictionary')
	print(f'{dictLength()}')
elif menu == '10':
	print('10. Add, remove and empty a dictionary')
	print(f'{addRemoveEmptyDict()}')
elif menu == '11':
	print('11. create a dictionary with the dict() constructor')
	print(f'{createNewDict}')
else:
  print('Menu not found, choose 1-11 only!')

printLine()
print('Thank you...')