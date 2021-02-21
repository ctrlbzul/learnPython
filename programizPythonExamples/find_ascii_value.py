'''
ASCII stands for American Standard Code for Information Interchange.
It is a numeric value given to different characters and symbols, for computers to store and manipulate. For example, the ASCII value of the letter 'A' is 65.
'''

# program to find the ASCII value of the given character
char = 'p'
print('The ASCII value of {0} is {1}'.format(char, ord(char)))

''''
ord() = function to convert a character to an integer (ASCII value). This function returns the Unicode code point of that character.
'''

'''
MY TURN
Modify the code above to get characters from their corresponding ASCII values using the chr() function

chr() = function that returns the character that represents the specified unicode.
'''

# program to find the character of a unicode
char1 = chr(65)
char2 = chr(120)
char3 = chr(ord('S') + 1)

# print the result
print(f'''
>>> chr(65)
'{char1}'
>>> chr(120)
'{char2}'
>>> chr(ord('S') + 1)
'{char3}'
''')
