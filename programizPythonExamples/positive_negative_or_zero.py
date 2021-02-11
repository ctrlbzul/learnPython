# Python Program to Check if a Number is Positive, Negative or 0

# using if..elif..else
num = float(input('Enter a number\t: '))
if num > 0:
	print('{0} is a positive number.'.format(num))
elif num == 0:
	print('{0} is zero number.'.format(num))
else:
	print('{0} is a negative number.'.format(num))

# uncomment below to use code
# using nested if
num = float(input('Enter a number\t: '))
if num >= 0:
	if num == 0:
		print('{0} is zero number.'.format(num))
	else:
		print('{0} is a positive number.'.format(num))
else:
	print('{0} is a negative number.'.format(num))
