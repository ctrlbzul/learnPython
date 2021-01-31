# import math module (for pow function)
import math

print("[ ELIF SIMPLE CALCULATOR ]")
print("[ OPERATOR : + - * / % ^ ]\n")
print("--------------------------------------")

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

	print('result : ', firstNum, _operator, secondNum, ' = ', result)
	
	print("--------------------------------------------------")
	again = str(input("Calculate again ?(y/n) : "))
	if again == "n" or again == "N":
		break

print("Thanks :)")
