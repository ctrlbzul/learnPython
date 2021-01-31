# factorial is written with ! (ex : factorial of 5 = 5!)
def factorialValue(num_param):
	factorial = 1

	# with while loops
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
			factorial*=i
			i+=1
		print(num_param, "! =", factorial)

while True:
	num = int(input("Input an integer number : ")) # num = number
	factorialValue(num)

	# program's loop
	again = str(input("Wanna use program again ? (y/n): "))
	if again == "n" or again == "N" or again != "y":
		break 

print("Thank You..")
