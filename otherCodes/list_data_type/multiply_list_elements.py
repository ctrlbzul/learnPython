# python3 program to multiply all values in the list

'''
function : iterate through the array and multiply each element
return int (result)
'''
def multiplyList(my_list):
	result = 1
	# multiply element one by one
	for element in my_list:
		result = result * element
	return result

'''
function : print array elements with plus sign (*)
return string
'''
def listMultiplySign(my_list):
  string_list = map(str, my_list)

  multiply_sign = ' * '
  multiply_sign = multiply_sign.join(string_list)
  return multiply_sign

# user code
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(f'''Input : list1 = {list1}\
	\nOutput : {multiplyList(list1)}\
	\nExplanation : {listMultiplySign(list1)}''')
print()
print(f'''Input : list2 = {list2}\
	\nOutput : {multiplyList(list2)}\
	\nExplanation : {listMultiplySign(list2)}''')
