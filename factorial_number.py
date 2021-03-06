# Python 3 program to find factorial of given number
	
# factorial is written with ! (ex : factorial of 5 = 5!)
def factorial(n_param):
  # uncomment code below to use factorial function with recursive
  # if n_param < 0:
  #   return 0
  # elif n_param == 0 or n_param == 1:
  #   return 1
  # else:
  #   return n_param * factorial(n_param - 1)

	# uncomment code below to use factorial function with while loops
  # fact = 1
  # i = 1
  # while (i <= n_param):
  #   fact *= i
  #   i += 1
  # return fact

	# uncomment code below to use factorial function with iterative
	# def factorial(n_param):
	#   if n_param < 0:
	#     return 0
	#   elif n_param == 0 or n_param == 1:
	#     return 1
	#   else:
	#     fact = 1
	#     while (n_param > 1):
	#       fact *= n_param
	#       n_param -=1
	#     return fact

	# uncomment code below to use factorial function with for loops
	# if n_param < 0:
	# 	return 0
	# elif n_param == 0 or n_param == 1:
	# 	return 1
	# else:
	# 	for i in range(1, n_param+1): # factorial+1 for end value
	# 		fact *= i
	# 		# i += 1
	# 	return fact

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
