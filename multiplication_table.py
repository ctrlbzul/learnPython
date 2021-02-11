# multipication table from 1 to 10

# function to iterate number 10 times
# from i = 1 to 10
def mult_table(number_param):
	for i in range(1, 11):
		print('{0} x {1}\t= {2}'.format(number_param, i, (number_param*i)))

print('// MULTIPLICATION TABLE 1-10 //')
print('-----------------------------------')
try:
	number = int(input('Display multiplication table of : '))
	mult_table(number)
except :
	print('Input is not an integer!')
