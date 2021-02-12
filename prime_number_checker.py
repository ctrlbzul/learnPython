# function to print straight line
def printLine():
	print("-----------------------------------")

# function to check prime number
def prime_number(num_param):
	if num_param > 1:
		# check for division factors
		for i in range(2,num_param):
			if num_param % i == 0:
				print("{0} is not a prime number.".format(num_param))
				# (//) = the floor division (rounds the result down to the nearest whole number)
				print("{0} x {1} is {2}".format(i, num_param//i, num_param))
				break
		else:
			print("{0} is a prime number.".format(num_param))
	# if number is <= 1, then it's not a prime numbers
	else:
		print("{0} is not a prime number.".format(num_param))

while True:
	print("\n// Prime Numbers Check //")
	printLine()
	num = int(input("Enter a number\t: "))
	prime_number(num)

	# program loops confirmation
	printLine()
	again = str(input("Use program again ? (y/n): "))
	if again == "n" or again == "N" or again != "y":
		break

print("Thank you..")
