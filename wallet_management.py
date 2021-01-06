class myWallet:
  money = 0 #$ (dollar)

  def set_money(self, set): # set (default) money
    self.money = set
    return self.money 

  def greet(self): # show current money
    print('You HAVE', self.money, '$ in my wallet\n')

  def add_money(self, count):
    self.money += count
    print(count, '$ ADDED\nNow You have', self.money, '$ in my wallet')

  def take_money(self, money_taken):
    if money_taken > self.money:
      print('You DON\'T have that much money!')
    elif money_taken == self.money:
      print('Your wallet is now EMPTY')
    else:
      self.money -=  money_taken
      print(money_taken, '$ TAKEN\nmoney in your wallet now :', self.money, '$')

manage_money = myWallet() # make instance

print('[ WALLET\'S\' MANAGEMENT ]\n')
my_money = int(input('Set your money : '))
print('MY MONEY :', manage_money.set_money(my_money), '$')

manage = input('Input m to manage money : ')
if manage == 'm' or manage == 'M':
  manage_money.greet()

  print('[ Manage Menu : 1. ADD MONEY  2. TAKE MONEY ]')
  choose = input('input 1 or 2 : ')
  if choose == '1':
    add_count = int(input('Add money : '))
    manage_money.add_money(add_count)
  elif choose == '2':
    take_count = int(input('Take money : '))
    manage_money.take_money(take_count)
  else:
    print('You can manage your money anytime!')  

print('\nThank You\n')

