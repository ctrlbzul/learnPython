# function : to print binary number using recursion
def convertToBinary(num_param):
  if num_param > 1:
    convertToBinary(num_param // 2)
  print(num_param % 2, end = '')

# decimal
dec_num = 34

# uncomment code below to take user input
# dec_num = int(input('Enter a decimal number : '))

convertToBinary(dec_num)
print() # newline
