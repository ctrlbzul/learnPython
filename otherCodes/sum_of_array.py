# python 3 code to find sum of elements in given array 

# function : iterate through the array and add each element to the sum variable
def sumArray(array):
  # variable to store sum of array
  sum = 0

  for i in array:
    sum += i
  return sum

# initiate array
arr = []
# input values to array
arr = [15, 12, 13, 10]

# get sum of array
sum_of_array = sumArray(arr)
# calculate length of array
array_length = len(arr)

# print length and sum of array
print(f'Array : {arr}\nLength : {array_length}\nSum of array is : {sum_of_array}')
