def prime_number(num_param):
	if num_param > 1:
		# check for division factors
		for i in range(2,num_param):
			if num_param % i == 0:
				print(num_param, "is not a prime number.")
				print(i,"x",num_param//i,"is",num_param)
				break
		else:
			print(num_param, "is a prime number.")
	# if number is <= 1, then
	# it's not a prime numbers
	else:
		print(num_param, "is not a prime number")

print("// Prime Numbers Check //")
print("/////////////////////////\n")

num = int(input("input a number : "))
prime_number(num)
