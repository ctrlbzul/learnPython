# A matrix
A = [[2, 4],
		 [6, 8],
		 [10, 12]]

# R matrix (transposed matrix)
R = [[0, 0, 0],
		 [0, 0, 0]]

''' expected output :
[2, 6, 10]
[4, 8, 12]'''

# transpose the A matrix
# iterate through rows
for i in range(len(A)):
	# iterate through columns
	for j in range (len(A[0])):
		R[j][i] = A[i][j]

# print transposed A matrix
for item in R:
	print(item)