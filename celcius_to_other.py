# degree symbol
degree_sym = u'\N{DEGREE SIGN}' # degree symbol

# function to print a straight line
def printLine():
	print('----------------------------------------')

# function to convert celcius to reamur
def toReamur(celcius_param):
  print('{0}{1} = {2}{3}'.format(celcius_param, (degree_sym + 'C'), ((4/5)*celcius_param), (degree_sym + 'R')))

# function to convert celcius to fahrenheit
def toFahrenheit(celcius_param):
  print('{0}{1} = {2}{3}'.format(celcius_param, (degree_sym + 'C'), (celcius_param*(9/5) + 32), (degree_sym + 'F')))

# function to convert celcius to kelvin
def toKelvin(celcius_param):
  print('{0}{1} = {2}{3}'.format(celcius_param, (degree_sym + 'C'), (celcius_param + 273.15), (degree_sym + 'K')))

print('// CELCIUS CONVERTER //')
print('1. Celcius to Reamur\n2. Celcius to Fahrenheit\n3. Celcius to Kelvin')
printLine()

while True:
	# get celcius value input
	c_value = float(input('Input temperature in Celcius\t: '))

	# convert the celcius value
	converter = input('Choose converter (1/2/3)\t: ')
	if converter == '1':
		toReamur(c_value)
	elif converter == '2':
		toFahrenheit(c_value)
	elif converter == '3':
		toKelvin(c_value)
	else:
		print('PLEASE CHOOSE BETWEEN 1-3!')

	printLine()
	again = str(input("Convert celcius again ?(y/n)\t: "))
	if again == "n" or again == "N":
		break

print("Thanks :)")

  


