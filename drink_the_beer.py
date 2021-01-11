class beer():

	def __init__(self):
		self.liter_beer = 3.0 # liter

	def drink_beer(self, beer_drunk):
		if beer_drunk > self.liter_beer:
			print('You ONLY have', self.liter_beer, 'liter beer.')
		elif beer_drunk == self.liter_beer:
			print('You drunk ALL the beer OUT!\nCareful, You maybe HIGH right now!')
		else:
			self.liter_beer -= beer_drunk
			print('You DRUNK', beer_drunk, 'liter beer.')
			print(self.liter_beer, 'liter beer left.')

			while self.liter_beer < 3.0:
				drink_again = str(input('Wanna drink AGAIN ? (y/n): '))
				if drink_again == 'y':
					beer_again = float(input('How much beer that you NEEDED AGAIN ?: '))
					self.liter_beer -= beer_again
					print('You DRUNK', beer_drunk, 'liter beer.')
					print(self.liter_beer, 'liter beer left.')
					if self.liter_beer == 0.0:
						print('You drunk ALL the beer OUT!\nCareful, You maybe HIGH right now!')
				else:
					break

drinker = beer() # make drinker instance

wanted_beer = float(input('HOW MUCH beer you want to drink ?: '))
drinker.drink_beer(wanted_beer)
print('\nThanks Mate!')
