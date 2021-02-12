class myWallet:
	money = 0 # default amount of money

	# function set money
	def set_money(self, set):
		self.money = set
		return self.money 

	# function to show current money
	def greet(self):
		print('Money in your wallet\t: {0}$'.format(self.money))

	# function to adding money
	def add_money(self, count):
		self.money += count
		print('{0}$ ADDED\nNow You have {1}$ in your wallet'.format(count, self.money))

	# function to taking money
	def take_money(self, money_taken):
		if money_taken > self.money:
			print('You DON\'T have that much money!')
		elif money_taken == self.money:
			print('Your wallet is now EMPTY')
		else:
			self.money -=  money_taken
			print('{0}$ TAKEN\nmoney in your wallet now : {1}$'.format(money_taken, self.money))

# function to print a straight line
def printLine():
	print('-----------------------------------')

# make an instance from myWallet class
manage_money = myWallet()

print('[ WALLET MANAGEMENT ]')
printLine()
my_money = int(input('Set your money\t: '))
print('MY MONEY\t: {0}$'.format(manage_money.set_money(my_money)))

printLine()
manage = input('Enter m to manage money\t: ')
if manage == 'm' or manage == 'M':
	manage_money.greet()
	printLine()
	print('[ Manage Menu\t: 1. ADD MONEY  2. TAKE MONEY ]')

	while(input != '1' or input != '2'):
		choose = input('input 1 or 2\t: ')
		if choose == '1':
			add_count = int(input('Add money\t: '))
			manage_money.add_money(add_count)
			break
		elif choose == '2':
			take_count = int(input('Take money\t: '))
			manage_money.take_money(take_count)
			break
		else:
			print('Only input 1 or 2!')
		printLine()  
else:
	print('You can manage your money anytime!')
printLine()
print('Thank You')

