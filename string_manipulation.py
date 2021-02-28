# string manipulation program

# funtion : show menu
def showMenu():
  print('''1. Get character at position 1\
  \n2. Get characters from position x to y (y not included)\
  \n3. Remove whitespace\
  \n4. Return length of the string\
  \n5. Convert string to lower case\
  \n6. Convert string to uppercase\
  \n7. Replace string with another string\
  \n8. Split string (each word) into a list''')

# function : print a straight line
def printLine():
  print('------------------------------------------------------------')

# function : get character at position 1 (1)
def getCharPositionOne(string_param):
  return string_param[0]

# function : get character from position x to y (2)
def getCharPositionXY(string_param):
  x = int(input('position x : '))
  y = int(input('position y : '))
  return string_param[x:y]

# function : remove whitespaces (3)
def removeWhitespace(string_param):
  remove = string_param.strip(" \t")
  return remove

# function : return length of string (4)
def stringLength(string_param):
  return len(string_param)

# function : convert string to lower case (5)
def toUpperCase(string_param):
  return string_param.upper()

# function : convert string to upper case (6)
def toLowerCase(string_param):
  return string_param.lower()

# function : replace string with another string (7)
def replaceString(string_param):
  string_to_replace = str(input('String to replace : '))
  if string_to_replace in string_param:
    new_string = str(input('Replace string to : '))
    final_string = string_param.replace(string_to_replace, new_string)
  else:
    print('{} not found in your string'.format(string_to_replace))
  
  # return replaced string
  return (f'''Replace {string_to_replace} to {new_string}\
  \nYour string : {final_string}''')

# function to split string into a list where each word is a list item
def splitString(string_param):
  return string_param.split()

# MAIN DISPLAY
print('// STRING MANIPULATION //')
printLine()
showMenu()


# get user input (str)
printLine()
user_string = str(input('Input a string / sentence : '))
menu = input('Choose string manipulation menu (1-8) : ')
printLine()

# handling the menu
if menu == '1':
  print('1. Get character at position 1')
  getCharPositionOne(user_string)
elif menu == '2':
  print('2. Get characters from position x to y (y not included)')
  getCharPositionXY(user_string)
elif menu == '3':
  print('3. Remove whitespace')
  removeWhitespace(user_string)
elif menu == '4':
  print('4. Return length of the string')
  stringLength(user_string)
elif menu == '5':
  print('5. Convert string to lower case')
  toLowerCase(user_string)
elif menu == '6':
  print('6. Convert string to uppercase')
  toUpperCase(user_string)
elif menu == '7':
  print('7. Replace string with another string')
  replaceString(user_string)
elif menu == '8':
  print('8. Split string (each word) into a list')
  splitString(user_string)

