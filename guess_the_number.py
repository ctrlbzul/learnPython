import random

random_number = random.randint(1, 5)

while True:
	guess = int(input("There is random number between 1 and 5,\nGUESS THE NUMBER : "))
	if guess == random_number:
		print("CORRECT! the random is", random_number)
		break
	else:
		print("Wrong, try again!")

