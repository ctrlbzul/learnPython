# factorial is written with ! (ex : factorial of 5 = 5!)
def factorialValue(num_param):
	factorial = 1

	# uncomment to use factorial function with while loops
	# i = 1
	# while i <= number:
	# 	result*=i
	# 	i+=1

	# with for loops
	if num_param < 0:
		print("ERROR : Factorial does'nt exist for NEGATIVE NUMBERS")
	elif num_param == 0:
		print("0! = 1")
	else:
		for i in range(1, num_param+1): # factorial+1 for end value
			factorial *= i
			# i += 1
		print("{0}! = {1} (factorial of {2} is {3})".format(num_param, factorial, num_param, factorial))

while True:
	num = int(input("Enter an integer number : "))
	factorialValue(num)
	print('-----------------------------------')
	# ask for program's loop
	again = str(input("Use program again ? (y/n): "))
	if again == "n" or again == "N" or again != "y":
		break 

print("Thank You..")
