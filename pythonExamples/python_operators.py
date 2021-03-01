# string manipulation program

# funtion : show menu
def showMenu():
  print('''1. Addition operator\
  \n2. Substraction operator\
  \n3. Multiplication operator\
  \n4. Division operator\
  \n5. Modulus operator\
  \n6. Assignment operator''')

# function : print a straight line
def printLine():
  print('------------------------------------------------------------')

# function : addition operator (1)
def additionOperator(x_param, y_param):
  return (f'''x = {x_param}\
  \ny = {y_param}\
  \n>> x + y = {x_param + y_param}''')

# function : substraction operator (2)
def substractionOperator(x_param, y_param):
  return (f'''x = {x_param}\
  \ny = {y_param}\
  \n>> x - y = {x_param - y_param}''')

# function : multiplication operator (3)
def multiplicationOperator(x_param, y_param):
  return (f'''x = {x_param}\
  \ny = {y_param}\
  \n>> x * y = {x_param * y_param}''')

# function : division operator (4)
def divisionOperator(x_param, y_param):
  return (f'''x = {x_param}\
  \ny = {y_param}\
  \n>> x / y = {x_param / y_param:.3f}''')

# function : modulus operator (5)
def modulusOperator(x_param, y_param):
  return (f'''x = {x_param}\
  \ny = {y_param}\
  \n>> x % y = {x_param % y_param}''')

# function : assignment operator (6)
def assignmentOperator(x_param, y_param):
  return (f'''x = {x_param}\
  \ny = {y_param}\
  \n>> {x_param} assigned to x\
  \n>> {y_param} assigned to y''')

# MAIN DISPLAY
print('// PYTHON EXAMPLE : OPERATORS //')
printLine()
showMenu()

# get user input (str)
printLine()
print('''x = your first number\
\ny = your second number''')
printLine()
x = float(input('Input x : '))
y = float(input('Input y : '))
printLine()
menu = input('Choose the menu (1-6) : ')
printLine()

# handling menu input
if menu == '1':
  print('>> 1. Addition operator')
  print(f'{additionOperator(x, y)}')
elif menu == '2':
  print('>> 2. Substraction operator')
  print(f'{substractionOperator(x, y)}')
elif menu == '3':
  print('>> 3. Multiplication operator')
  print(f'{multiplicationOperator(x, y)}')
elif menu == '4':
  print('>> 4. Division operator')
  print(f'{divisionOperator(x, y)}')
elif menu == '5':
  print('>> 5. Modulus operator')
  print(f'{modulusOperator(x, y)}')
elif menu == '6':
  print('>> 6. Assignment operator')
  print(f'{assignmentOperator(x, y)}')
else:
  print('Menu not found, choose 1-6 only!')

printLine()
print('Thank you...')
