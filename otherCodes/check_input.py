'''
check for these input :
1. HelloWorld (all letters, nothing more, nothing less)
2. Hello World (pay attention to the space)
3. HelloWorld123 (both letters and/or numbers)
4. 123 (pure number, int)
5. 12.2 (floating point)
'''

# check if user input is all letters (alpha)
def isStringOnly(check_input):
	if check_input.isalpha():
		return(f'is the input all letters ? True')
	return(f'is the input all letters ? False')

# check if user input is all letters and contain any spaces
def isStringWithSpace(check_input):
	valid = False
	if ' ' in check_input:
		for letter in check_input:
			if letter.isdigit():
				valid = False
			elif letter.isalpha() or letter.isspace():
				valid = True
	return (f'is the input all letters with a space or two ? {valid}')

# check if user input is both letters and/or numbers
def isStringOrNum(check_input):
	if check_input.isalnum():
		return(f'is the input both letters and/or numbers ? True')
	return(f'is the input both letters and/or numbers ? False')

# user input
user_input = input('Type here : ')
print(f'''{isStringOnly(user_input)}\
	\n{isStringWithSpace(user_input)}\
	\n{isStringOrNum(user_input)}''')
	
