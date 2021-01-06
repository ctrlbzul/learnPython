print('[ ODD OR EVEN ]\n')

loop = 0
loopCount = input('Input loop count : ')
loopCount = int(loopCount)
while loop < loopCount: 
	inputNumber = int(input('Input Number : '))
	if (inputNumber % 2 == 0):
		print(str(inputNumber), ' is an even number.')
	elif (inputNumber %2 == 1):
		print(str(inputNumber), ' is an odd number.')
	else:
		print('ERROR : INPUT NUMBER ONLY!')
	loop += 1
print('\nThank You')