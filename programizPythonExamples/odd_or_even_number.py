# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input('Enter a number\t: '))
if num % 2 == 0:
  print('{0} is an even number'.format(num))
else:
  print('{0} is an odd number'.format(num))
