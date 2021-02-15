# Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
num1 = 10
num2 = 14
num3 = 12

# uncomment following lines to take three numbers from user
# num1 = float(input("Enter first number\t: "))
# num2 = float(input("Enter second number\t: "))
# num3 = float(input("Enter third number\t: "))

if (num1 >= num2) and (num1 >= num3):
  largest_num = num1
elif (num2 >= num1) and (num2 >= num3):
  largest_num = num2
else:
  largest_num = num3

print('The largest number is {}'.format(largest_num))
