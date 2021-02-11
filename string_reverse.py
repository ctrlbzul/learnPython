def reverse_string(my_string_param):
	'''
	In this particular example, the slice statement [::-1] means
	start at the end of the string and end at position 0,
	move with the step -1, negative one, which means one step backwards.
	'''
	return my_string_param[::-1]

print('// STRING REVERSER //')
print('----------------------------\n')

# input string 
my_string = str(input('Input the string\t: '))

# print reversed string
print('Reversed string\t\t: {0}'.format(reverse_string(my_string)))
