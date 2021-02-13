# function to print a straight line
def printLine():
	print('-----------------------------------')

class beer():
	# function to set the amount of beer
	def __init__(self):
		self.liter_beer = 3.0 # (liter)

	# function to take (drink) the beer
	def drink_beer(self, beer_to_drink):
		if beer_to_drink > self.liter_beer:
			print('You ONLY have {0} liter beer!'.format(self.liter_beer))
		elif beer_to_drink == self.liter_beer:
			print('You drunk ALL the beer!\nCareful, You maybe HIGH right now!')
		else:
			self.liter_beer -= beer_to_drink
			print('You DRUNK {0} liter beer.'.format(beer_to_drink))
			print('{0} liter beer left.'.format(self.liter_beer))

			while self.liter_beer < 3.0:
				printLine()
				drink_again = str(input('Wanna drink AGAIN ? (y/n): '))
				if drink_again == 'y':
					beer_again = float(input('How much beer that you NEEDED AGAIN ?: '))
					self.liter_beer -= beer_again
					print('You DRUNK {0} liter beer.'.format(beer_to_drink))
					print('{0} liter beer left.'.format(self.liter_beer))
					if self.liter_beer == 0.0:
						print('You drunk ALL the beer!\nCareful, You maybe HIGH right now!')
				else:
					break

# make drinker instance
drinker = beer()

# get input (amount of beer to drink)
wanted_beer = float(input('HOW MUCH beer you want to drink ?: '))
drinker.drink_beer(wanted_beer)

# end of program
printLine()
print('Thanks Mate!')
