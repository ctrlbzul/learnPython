# program : make a simple calculator

# function : adds two numbers
def add(a, b):
  return a + b

# function : substracts two numbers
def substract(a, b):
  return a - b

# function : multiplies two numbers
def mulitply(a, b):
  return a * b

# function : divides two numbers
def divide(a, b):
  return a / b

print('Select the operation.')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')

while True:
  # Take input from the user
  choice = input('\nEnter a choice (1/2/3/4)\t: ')

  # Check if choice is one of the four options
  if choice in ('1', '2', '3', '4'):
    num1 = float(input('Enter first number\t: '))
    num2 = float(input('Enter second number\t: '))

    if choice == '1':
      print(f'{num1} + {num2} = {add(num1, num2)}')
    elif choice == '2':
      print(f'{num1} - {num2} = {substract(num1, num2)}')
    elif choice == '3':
      print(f'{num1} * {num2} = {mulitply(num1, num2)}')
    elif choice == '4':
      print(f'{num1} / {num2} = {divide(num1, num2)}')
    break
  else:
    print('Invalid input!')
