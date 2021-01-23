# recursive addition, example :
# num1 = 1, num2 = 3 ===> 1+2+3 = 6
def recursive_addition(num1_param, num2_param):
	if num1_param == num2_param:
		return num2_param
	else:
		return (num1_param + recursive_addition(num1_param+1, num2_param))

# ask to run program more than once
while True:
	try:
		num1 = int(input("First number\t: "))
		num2 = int(input("Second number\t: "))
		for i in range(num1, num2+1):
			print(i, " + ", end='')
			if i == num2-1:
				print(i+1, " = ", end='')
				break
		print(recursive_addition(num1, num2))
	except:
		print("Input integer only!")
		break
	print("--------------------------------------------------")
	again = str(input("Use program again ?(y/n) : "))
	if again == "n" or again == "N":
		break

print("Thanks :)")