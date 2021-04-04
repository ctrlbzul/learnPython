# python program to find sum of elements in list
total = 0

# creating a list
a_list = [17, 5, 3, 5]

# Iterate each element in list and add them in variable 'total'
for element in range(0, len(a_list)):
	total += a_list[element]

# printing a list and total value
print(f'List elements : {a_list}')
print(f'Sum of all elements in list : {total}')
