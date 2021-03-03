# Program to sort alphabetically the words form a string provided by the user

my_str = 'Hello this Is an Example With cased letters'

# uncomment to take input from the user
# my_str = input('Enter a string : ')

# breakdown the string into a list of lower case words
words = [word.lower() for word in my_str.split()]

# sort the list
words.sort()

# print the sorted words
print('The sorted words are : ')
for word in words:
  print(word)

# Note : if wanna test the program, change the value of my_str
