# recursive function to find factorial of a number
def factorial(num_param):
	if num_param == 1:
		return 1
	else:
		return (num_param * factorial(num_param - 1))

# while loop (to use program more than once)
while True:
	try:
		num = int(input("Get factorial of : "))
		print("The factorial of", num, "is", factorial(num))
	except:
		print("Input integer only!")
		break

	print("--------------------------------------------------")
	again = str(input("Get factorial again ?(y/n) : "))
	if again == "n" or again == "N":
		break

print("Thanks :)")
