# function to print a straight line
def printLine():
  print('-----------------------------------')


print('[ NAME SPELLER ]')
printLine()
name = input('Input Name\t: ')
final_name = name.lower() # changing letter to lowercase
printLine()

# get name length
name_length = len(name)
# get the spelling of each letter
spellings = {'a':'ei', 'b':'bi', 'c':'si', 'd':'di', 'e':'i',
						 'f':'ef', 'g':'ji', 'h':'eich', 'i':'ai', 'j':'jei',
						 'k':'kei', 'l':'el', 'm':'em', 'n':'en', 'o':'ou',
						 'p':'pi', 'q':'kyu', 'r':'ar', 's':'es', 't':'ti',
						 'u':'yu', 'v':'vi', 'w':'dablyu', 'x':'eks', 'y':'wai',
						 'z':'zi', ' ':'space'}

print('Name lengths\t: {0} characters (with space)'.format(name_length))
print('Name spellings\t:')
for letter in final_name:
	for spell in spellings:
		if spell == letter:
			print('{0} = {1}'.format(letter, spellings[spell]))

printLine()
print('PROGRAM FINISHED')
