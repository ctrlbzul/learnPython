# Python 3 program to find factorial of given number
	
# factorial is written with ! (ex : factorial of 5 = 5!)
# factorial function with for loops
def factorial(n_param):
  fact = 1

  if n_param < 0:
    return 0
  elif n_param == 0 or n_param == 1:
    return 1
  else:
    for i in range(1, n_param + 1):
      fact *= i
    return fact

while True:
	# given number
	n = int(input("Enter an integer number : "))
	print(f'Factorial of {n} is {factorial(n)}')
	print('----------------------------------------')
	
	# ask for program's loop
	again = str(input("Use program again ? (y/n): "))
	if again == "n" or again == "N" or again != "y":
		break 

print("Thank You..")
