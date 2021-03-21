# function : check is input an integer or not
def isInteger(check_input):
  if check_input.isdigit():
    return True
  return False

# function : check is input a string or not
def isString(check_input):
  if check_input.isalpha():
    return True
  return False

# function : check is input a float or not
def isFloat(check_input):
  if '.' in check_input:
    split_input = check_input.split('.')
    if len(split_input) == 2 and split_input[0].isdigit() and split_input[1].isdigit():
      return True
  return False

# user code
user_input = input('Type anything : ')
if isInteger(user_input):
  print(f'Your input : {user_input}, is an integer.')
elif isString(user_input):
  print(f'Your input : {user_input}, is a string.')
elif isFloat(user_input):
  print(f'Your input : {user_input}, is a float.')
else:
  print(f'Your input : {user_input}, is a string.')
