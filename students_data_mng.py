# function to print a straight line
def printLine():
	print('---------------------------------------------')

print("// STUDENTS DATA MANAGEMENT //")
printLine()
print("Manage Data :\n1. Create file\n2. Read file\n3. Write file")
choice = str(input("Input choice (1/2/3) : "))
printLine()

if choice == "1":
	print("/ CREATE FILE /")
	while True:
		# create a new file
		file_name = str(input("File's name (without .txt): "))
		try:
			# "x" = Create - will create a file, returns an error if the file exist
			my_file = open(file_name + ".txt", "x")
			break
		except:
			confirm = str(input("File is already exist, overwrite? \n(will overwrite the entire file!) (y/n): "))
			if confirm == "y" or confirm == "Y":
				# "w" - Write - will overwrite any existing file's content
				my_file = open(file_name + ".txt", "w")
				break
			elif confirm == "n" or confirm == "N":
				print("Please create file with different names!")
	# after break from loop		
	print("File's created.")

elif choice == "2":
	print("/ READ FILE /")
	# open file
	read_file = str(input("Input file's name (.txt) : "))
	# "r" - Read - open file for reading
	file_to_read = open(read_file, "r")
	print('Opening file : {0}'.format(read_file))
	
	printLine()
	print('= {0} ='.format(read_file))
	print(file_to_read.read())
	file_to_read.close()
elif choice == "3":
	print("/ WRITE FILE /")
	write_file = str(input("Input file's name (.txt) : "))
	# "a" - Append - will append to the end of the file
	file_to_write = open(write_file, "a")

	data_count = int(input("How much data you want to write? : "))
	for i in range(0, data_count):
		data = str(input("Data : "))
		file_to_write.write("\n" + data)
	
# open and read the file after the wrote data :
	printLine()
	print(' = {0} ='.format(write_file))
	file_to_write = open(write_file, "r")
	print(file_to_write.read())
	file_to_write.close()
