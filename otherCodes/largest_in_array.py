'''
Python3 program to find maximum
in arr[] of size n
''' 

# function : find maximum in arr[] of size n
def largest(arr, n_param):
	# Initialize maximum element
	max = arr[0]
	
	'''
	Traverse array elements from second
  and compare every element with 
  current max
	'''
	for i in range(1, n):
		if arr[i] > max:
			max = arr[i]
	return max

# user code
arr = [20, 10, 20, 4, 100]
n = len(arr)
largest_in_array = largest(arr, n)
print(f'Largest in given array is {largest_in_array}')
