print("/ ODD - EVEN GENERATOR\t/")
print("/ 1. ODD\t\t/\n/ 2. EVEN\t\t/\n")

choices = int(input("Choose generator (1/2) : "))
if choices == 1:
	# creating empty odd list
	odd_list = []
	odd_start_num = int(input("Input start number\t: "))
	odd_end_num = int(input("Input end number\t: "))
	# number of odd elements to generate
	for i in range(odd_start_num, odd_end_num + 1):
		if i %2 != 0:
			odd_list.append(i) # adding the element (i)
	print("\nODD LIST")
	print(odd_list) # print the odd list

elif choices == 2:
	# creating empty odd list
	even_list = []
	even_start_num = int(input("Input start number\t: "))
	even_end_num = int(input("Input end number\t: "))
	# number of even elements to generate
	for i in range(even_start_num, even_end_num+1):
		if i %2 == 0:
			even_list.append(i)
	print("\nEVEN LIST")
	print(even_list) # print the even list

else:
	print("Choose only 1 or 2!")

			