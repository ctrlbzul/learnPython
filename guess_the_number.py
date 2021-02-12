# import random modules
import random
# generate random number in range of 1 to 5
random_number = random.randint(1, 5)

while True:
	print('There is random number between 1 and 5!')
	guess = int(input("GUESS THE NUMBER : "))
	if guess == random_number:
		print("CORRECT! the random number is {0}".format(random_number))
		break
	else:
		print("WRONG, try again!")

