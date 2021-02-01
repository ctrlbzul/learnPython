# recursive function to power raised a number
# returns the value of base_param raised to power exponent_param
def toThePowerOf(base_param, exponent_param):
	if exponent_param == 1:
		return base_param
	elif base_param == 1 or exponent_param == 0:
		return 1
	else:
		return (base_param * (toThePowerOf(base_param, exponent_param - 1)))

print('// POWER RAISE //')
# while loop (to use program more than once)
while True:

	base = int(input('Base number\t: '))
	exponent = int(input('Exponent\t: '))
	print('\n', end='')  # linebreak

	# error handling, if base is not a positive number
	if base < 0:
		print('ERROR : Base number must be positive number!')
		break

	# print the result
	result = toThePowerOf(base, exponent)
	print(base, 'raised to the power of', exponent, '=', result)
	print('-------------------------------------')

	# asking for loop
	again = input('Use program again ? (y/n)\t: ')
	if again == 'n' or again == 'N':
		break

print('Thank You..')
