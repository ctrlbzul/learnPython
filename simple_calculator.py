# import math module (for pow function)
import math

# print straight line
def printLine():
	print("--------------------------------------")

print("[ ELIF SIMPLE CALCULATOR ]")
print("[ OPERATOR : + - * / % ^ ]")
printLine()

while True:
	firstNum = int(input('input first number  : '))
	_operator = input('input operator : ')
	secondNum = int(input('input second number : '))

	if (_operator == '+'):
		result = firstNum + secondNum # addition
	elif (_operator == '-'):
		result = firstNum - secondNum # substraction
	elif (_operator == '*'):
		result = firstNum * secondNum # multiplication
	elif (_operator == '/'):
		result = float(firstNum / secondNum) # division
	elif (_operator == '%'):
		result = firstNum % secondNum # modulo
	elif (_operator == '^'):
		result = math.pow(firstNum, secondNum) # power
	else:
		print('ERROR : unknown operator!')
		break

	print('{0} {1} {2} = {3}'.format(firstNum, _operator, secondNum, result))
	
	printLine()
	again = str(input("Calculate again ?(y/n) : "))
	if again == "n" or again == "N":
		break

print("Thanks :)")
