# recursive function to power raised a number
def toThePowerOf(base_param, power_param):
  if power_param == 1:
    return base_param
  else:
    return (base_param * (toThePowerOf(base_param, power_param - 1)))

# while loop (to use program more than once)
while True:

  print('// POWER RAISE //')
  base = int(input('Base number\t: '))
  power = int(input('Power\t\t: '))
  print('\n', end='') # linebreak

  # print the result
  result = toThePowerOf(base, power)
  print(base, 'to the power of', power, '=', result)

  again = input('\nUse program again ? (y/n)\t: ')
  if again == 'n' or again == 'N':
    break
  print('------------------------------------')

print('Thank You..')
