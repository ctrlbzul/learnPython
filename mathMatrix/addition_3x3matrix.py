# Program to add two 3x3 matrices using nested loop
# matrix A
A = [[1, 2, 3],
     [4, 5, 6],
	   [7, 8, 9]]

# matrix B
B = [[9, 8, 7],
     [6, 5, 4],
	   [3, 2, 1]]

# matrix R (matrix A + matrix B)
R = [[0, 0, 0],
	   [0, 0, 0],
	   [0, 0, 0]]

'''
expected output:
[10, 10, 10]
[10, 10, 10]
[10, 10, 10]
'''

# iterate through rows
for i in range(len(A)):
	# iterate through columns
	for j in range(len(A[0])):
		R[i][j] = A[i][j] + B[i][j]

# print all matrices
print('// MATRIX A //')
for item in A:
	print(item)

print('\n// MATRIX B //')
for item in B:
	print(item)

print('\nMATRIX R = MATRIX A + MATRIX B')
print('// MATRIX R //')
for item in R:
	print(item)
