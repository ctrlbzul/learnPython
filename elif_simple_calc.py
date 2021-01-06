print("[ ELIF SIMPLE CALCULATOR ]")
print("[ OPERATOR : + - * / % ^ ]\n")

firstNum = int(input('input first number  : '))
_operator = input('input operator : ')
secondNum = int(input('input second number : '))

if (_operator == '+'):
	result = firstNum + secondNum
elif (_operator == '-'):
	result = firstNum - secondNum
elif (_operator == '*'):
	result = firstNum * secondNum
elif (_operator == '/'):
	result = float(firstNum / secondNum)
elif (_operator == '%'):
	result = firstNum % secondNum
elif (_operator == '^'):
	result = firstNum
else:
	print('ERROR : unknown operator!')

print('result : ', firstNum, _operator, secondNum, ' = ', result)

print('\nTHANK YOU...')