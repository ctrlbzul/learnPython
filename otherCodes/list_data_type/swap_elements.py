# python3 program to swap elements at given positions

# function : swap
def swapPositions(a_list, pos1, pos2):
	a_list[pos1], a_list[pos2] = a_list[pos2], a_list[pos1]
	return a_list

a_list = [1, 2, 3, 4, 5]
pos1, pos2 = 2, 5

print(f'''Input\t: List = {a_list}\
	\nOutput\t: {swapPositions(a_list, pos1-1, pos2-1)}''')
