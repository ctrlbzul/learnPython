'''
function : iterate through the array and add each element to the sum variable
return int (sum)
'''
def sumArray(array):
  # variable to store sum of array
  sum = 0
  for i in array:
    sum += i
  return sum

'''
function : print array elements with plus sign (+)
return string
'''
def arrayPlusSign(array):
  string_array = map(str, array)

  plus_sign = ' + '
  plus_sign = plus_sign.join(string_array)
  return plus_sign

'''
function : print a straight line
return string
'''
def printLine():
  return(f'----------------------------------------')

# initiate array (empty list)
print(f'// SUM OF ARRAY //\n{printLine()}')
arr = []
# ask user input for array elements
count = int(input('Element count : '))
for i in range(0, count):
  elements = int(input(f'Input element [{i}] : '))
  arr.append(elements)

print(f'{printLine()}')
# get sum of array
sum_of_array = sumArray(arr)
# calculate length of array
array_length = len(arr)

# print length and sum of array
print(f'Array\t: {arr}\nLength\t: {array_length}\nSum\t: {arrayPlusSign(arr)}\nSum of array : {sum_of_array}')
