# program : factorial of a number using recursion

def recursiveFactorial(num_param):
	if num_param == 1:
		return num_param
	else:
		return num_param * recursiveFactorial(num_param - 1)

num = 7

# uncomment code below to take input from user
# num = int(input('Enter a number : '))

# check for negative or zero (0) numbers
if num < 0:
	print('Sorry, factorial does not exist for negative numbers')
elif num == 0:
	print('The factorial of 0 is 1')
else:
	print(f'The factorial of {num} is {recursiveFactorial(num)}')
