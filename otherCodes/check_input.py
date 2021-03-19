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
	user_input = input(f'Guess the number between {min_num} and {max_num} : ')

	# check for user input error
	while True:
		# check if input is an integer and within the range
		if user_input.isdigit():
			if int(user_input) in range(min_num, max_num + 1):
				break
			elif int(user_input) not in range(min_num, max_num + 1):
				user_input = input(f'Please, input the number between {min_num} and {max_num} : ')
		else:
			print(f'Error : please input an integer!')
			user_input = input(f'Guess the number between {min_num} and {max_num} : ')
			
	input_result = int(user_input)
	return input_result

# MAIN CODE
print('>> GUESS THE NUMBER')
printLine()

# define guessing range
low = 0
high = 7

# if player wanna decide the guessing range.
# low = int(input('Input low guessing range : '))
# high = int(input('Input high guessing range : '))

computer_choice = computerNumber(low, high)
player_choice = playerGuess(low, high)

# loop until player guesses the right number.
# while computer_choice != player_choice:
# chance
tired = 0
while True:
	# if guessed number wrong 3 times, ask for quit
	if tired == 3:
		give_up = input('Tired of guessing ? Wanna quit ? (y/n) : ')
		if give_up == 'y' or give_up == 'Y':
			print(f'You are giving up. The right number is {computer_choice}.')
			break

	if player_choice > computer_choice:
		player_choice = int(input('Number is too high, try again\t: '))
		tired += 1
	elif player_choice < computer_choice:
		player_choice = int(input('Number is too low, try again\t: '))
		tired += 1
	else:
		# if player guesses the right number, out from while loop
		printLine()
		print(f'CONGRATULATIONS! You guess the right number : {computer_choice}.')
		break
