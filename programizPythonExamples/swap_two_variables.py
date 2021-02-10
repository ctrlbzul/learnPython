# python program to swap to variables

x = 5
y = 9
# before swapping
print('Before swapping\t: x = {0} and y = {1}'.format(x,y))

# uncomment below to take the input from the user
# x = input('Enter value of x\t: ')
# y = input('Enter value of x\t: ')

# create a temporary variable and swap the values
temp = x # temp = 5
x = y # x = y(9)
y = temp # y = x(temp) = 5

print('The value of x after swapping\t: {}'.format(x))
print('The value of y after swapping\t: {}'.format(y))
