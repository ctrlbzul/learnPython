# function to demonstrate printing pattern
def pattern(n_param):

	# outer i loop to handle number of rows (n)
	for i in range(0, n_param):

		# innet loop to handle number of columns
		# values changing according to outer loop
		for j in range(0, i+1):
			# printing stars
			print('*', end='')
	
		# linebreak after each 
		print('\r')

# take input
n = int(input('Number of n\t: '))
print('------------------------------')
# assign n to function
pattern(n)

'''
expected output (n = 5):
*
**
***
****
*****
'''
