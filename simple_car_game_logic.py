user_input = ''
car_started = False

while True:
	user_input = input('> ').lower()

	if user_input.lower() == 'start':
		if car_started:
			print('Car already started!')
		else:
			car_started = True
			print('Car started...Ready to go!')
	elif user_input.lower() == 'stop':
		if not car_started:
			print('Car already stopped!')
		else:
			car_started = False
			print('Car stopped.')
	elif user_input.lower() == 'help':
		print('''\
		\nstart - to start the car\
		\nstop - to stop the car\
		\nquit - to exit
		''')
	elif user_input.lower() == 'quit':
		break
	else:
		print("Sorry, I don't understand that...")
