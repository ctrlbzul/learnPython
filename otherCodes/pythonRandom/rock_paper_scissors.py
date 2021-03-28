from random import randint

# function : print a straight line
def printLine():
  return(f'---------------------------------------------')

'''function : show options and ask for player choice
return int'''
def userInterface(options):
  for index, option in enumerate(options):
    print(f'{index} = {option}')
  
  user_input = int(input('What do u choose ? '))
  return user_input

'''function : generate a random number for computer choice
return random int'''
def computerChoice(content):
  computer_chose = randint(0, len(content)-1)
  return computer_chose

'''function : check who won
return string'''
def checkResults(choices, player, computer):
  if player == computer:
    return 'It\'s a tie.'
  elif (player == 0 and computer == len(choices)-1) or (player > computer and not(player == len(choices)-1 and computer == 0)):
    return 'Player WON, Computer LOST'
  return 'Player LOST, Computer WON'


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

  # check the results and print the winner
  results = checkResults(options_list, player_result, computer_result)
  print(f'{printLine()}\n{results}')

def main():
  # force player into the play loop
  play_again = ''
  while play_again.lower() != 'n':
    play()
    print(f'{printLine()}\nDo u want to play again ?')
    play_again = input('type \'y\' for yes or \'n\' for no : ')

main()
