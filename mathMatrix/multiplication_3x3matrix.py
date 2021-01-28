# Program to multiply two 3x3 matrices using nested loop
# A matrix
A = [[1, 2, 3],
		 [4, 5, 6],
		 [7, 8, 9]]

# B matrix
B = [[9, 8, 7],
		 [6, 5, 4],
		 [3, 2, 1]]

# R matrix (A matrix + B matrix)
R = [[0, 0, 0],
		 [0, 0, 0],
		 [0, 0, 0]]

'''
expected output:
[9, 16, 21]
[24, 25, 24]
[21, 16, 9]
'''

# iterate through rows
for i in range(len(A)):
	# iterate through columns
	for j in range(len(A[0])):
		R[i][j] = A[i][j] * B[i][j]

# print all matrices
# Matrix A
print('// MATRIX A //')
for item in A:
	print(item)

# Matrix B
print('\n// MATRIX B //')
for item in B:
	print(item)

print('\nMATRIX R = MATRIX A x MATRIX B')
print('// MATRIX R //')
for item in R:
	print(item)