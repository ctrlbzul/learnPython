from random import randint

def printLine():
	# function : print a straight line
	print('--------------------------------------------------')

def computerNumber(min_num, max_num):
	'''
	function : generates a random number based on the args (min_num, max_num).
	return random int
	'''
	return randint(min_num, max_num)

def playerGuess(min_num, max_num):
	'''
	function : asks the player to guess a number.
	return user_input
	'''
	user_input = int(input(f'Guess the number between {min_num} and {max_num} : '))
	# check for user errors
	while True:
		if isinstance(user_input, int) and user_input in range(min_num, max_num+1):
			break
		elif user_input not in range(min_num, max_num + 1):
			user_input = int(input(f'Please, input the number betwween {min_num} and {max_num} : '))
			
		# not yet handling string input
	
	return user_input

def play():
	print('>> GUESS THE NUMBER')
	printLine()
	# define guessing range
	low = 0
	high = 5

	computer_choice = computerNumber(low, high)
	player_choice = playerGuess(low, high)

	# loop until player guesses the right number.
	while computer_choice != player_choice:
		if player_choice > computer_choice:
			player_choice = int(input('Number is too high, try again\t: '))
		elif player_choice < computer_choice:
			player_choice = int(input('Number is too low, try again\t: '))

	# if player guesses the right number
	printLine()
	print(f'CONGRATULATIONS! You guess the right number : {computer_choice}')

# start the guessing game
play()
