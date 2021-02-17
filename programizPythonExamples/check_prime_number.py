# Program to check if a number is prime or not

num = 407

# uncomment to take input from user
# num = float(input('Enter a number\t: '))

# prime number are greater than 1
if num > 1:
  # check for factors
  for i in range(2, num):
    if (num % i) == 0:
      print('{} is not a prime number.'.format(num))
      print('{0} times {1} is {2}.'.format(i, num//i, num))
      break
  else:
    print('{} is a prime number.'.format(num))

# if input number is less than
# or equal to 1, it is not prime
else:
  print('{} is not a prime number.'.format(num))
