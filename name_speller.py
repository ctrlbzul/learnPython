print('[ NAME SPELLER ]\n')

name = input('Input Name	: ')
name2 = name.lower() # changing letter to lowercase

name_length = len(name)
spellings = {'a':'ei', 'b':'bi', 'c':'si', 'd':'di', 'e':'i',
						 'f':'ef', 'g':'ji', 'h':'eich', 'i':'ai', 'j':'jei',
						 'k':'kei', 'l':'el', 'm':'em', 'n':'en', 'o':'ou',
						 'p':'pi', 'q':'kyu', 'r':'ar', 's':'es', 't':'ti',
						 'u':'yu', 'v':'vi', 'w':'dablyu', 'x':'eks', 'y':'wai',
						 'z':'zi', ' ':'space'}

print('\nName lengths 	:', name_length, ' character (with space)')
print('Name spellings	:')
for letter in name2:
	for spell in spellings:
		if (spell == letter):
			print(letter, ' = ', spellings[spell])

print('\nPROGRAM FINISHED')