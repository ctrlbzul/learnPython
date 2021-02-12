# function to demonstrate printing pattern
def pattern(n_param):
	star_pattern = []
	for i in range(1, n_param+1):
		star_pattern.append('*' * i)
	print('\n'.join(star_pattern))

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
