'''function : sort a list from the smallest number
return list'''
def findSmallestNumber(my_list):
	my_list.sort()
	return my_list[0]

# create a list
a_list = [5, 4, 3, 12, 10, 8]

# find smallest number in the list
smallestNum = findSmallestNumber(a_list)
print(f'''List : {a_list}\
	\nSmallest number in list : {smallestNum}''')
