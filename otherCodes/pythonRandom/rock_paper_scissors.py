from random import randint

def printLine():
  return(f'---------------------------------------------')

def userInterface(options):
  for index, option in enumerate(options):
    print(f'{index} = {option}')
  
  user_input = int(input('What do u choose ? '))
  return user_input

def computerChoice(content):
  computer_chose = randint(0, len(content)-1)
  return computer_chose

def play():
  print(f'''{printLine()}\nWelcome to Rock, Paper, Scissors.\nPlease pick your weapon.''')

  # define the options (list), ask user to pick and randoming computer choice
  options_list = ['Rock', 'Paper', 'Scissors']
  player_result = userInterface(options_list)
  computer_result = computerChoice(options_list)

  # see what both parties chose
  print(f'{printLine()}')
  print(f'Player chose\t: {options_list[player_result]}')
  print(f'Computer chose\t: {options_list[computer_result]}')

play()
