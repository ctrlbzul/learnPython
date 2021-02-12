# lambda function to print a straight line
printLine = lambda : print('-----------------------------------------------------------------')
# how to use lambda = lambda arguments: expression
# lambda function uppercase and lowercase
toUpperCase = lambda x: x.upper() 
toLowerCase = lambda x: x.lower()

# lambda function to print the output
upperLowerCount = lambda x,y,z : print(
	"Uppercase letter\t= {0}\nLowercase letter\t= {1}\nSpace letter\t\t= {2}".format(x, y, z))

# default count of space, uppercase and lowercase letter
upper_letter = 0
lower_letter = 0
space_count = 0

print("[ UPPER CASE AND LOWER CASE GENERATOR ]")
print("[ 1.To Upper Case     2.To Lower Case ]")
printLine()

# get user input
txt = str(input("Paste/type your text here\t: "))
choose = str(input("Choose generator (1/2)\t: "))
if choose == "1":
	# print original string in uppercase
	print("\nUppercase string\t: ",toUpperCase(txt))
elif choose == "2":	
	# print original string in lowercase
	print("\nLowercase string\t: ",toLowerCase(txt))
else:
	print("ERROR : Only choose 1 or 2!")

# checking the inputted string
for a in txt:
	# checking for uppercase letter
	if(a.isupper() == True):
		upper_letter += 1
	# checking for lowercase letter
	elif(a.islower() == True):
		lower_letter += 1
	# checking for space/whitespace letter
	elif(a.isspace() == True):
		space_count += 1

# print the count of uppercase, lowercase and whitespace letter
upperLowerCount(upper_letter, lower_letter,space_count)
printLine()
