degree_sym = u'\N{DEGREE SIGN}' # degree symbol
def toReamur(celcius_param):
  print(celcius_param, (degree_sym + 'C'), ' = ', (4/5)*celcius_param, (degree_sym + 'R'), sep='')

def toFahrenheit(celcius_param):
  print(celcius_param, (degree_sym + 'C'), ' = ', celcius_param*(9/5) + 32, (degree_sym + 'F'), sep='')

def toKelvin(celcius_param):
  print(celcius_param, (degree_sym + 'C'), ' = ', celcius_param + 273.15, (degree_sym + 'K'), sep='')

print('/// CELCIUS CONVERTER ///')
print('1. Celcius to Reamur\n2. Celcius to Fahrenheit\n3. Celcius to Kelvin')
print('/////////////////////////\n')

# input celcius value
c_value = float(input('Input temperature in Celcius : '))

#convert the celcius value
converter = input('Choose converter (1/2/3) : ')
if converter == '1':
  toReamur(c_value)
elif converter == '2':
  toFahrenheit(c_value)
elif converter == '3':
  toKelvin(c_value)
else:
  print('PLEASE CHOOSE BETWEEN 1-3!')
  


