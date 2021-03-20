'''
// python program to find area of a circle //
area of circle = pi * r * r
where r is radius of circle
'''

# function to check is r an integer or not
def isInteger(check_r):
	if check_r.isdigit():
		return True
	return False

# function to check is r a floating number or not
def isFloat(check_r):
	if '.' in check_r:
		return True
	return False

def findArea(r):
	pi = 3.142
	while True:
		if not isInteger(r) and not isFloat(r):
			r = input('Please input integer or float only : ')
		else:
			r = float(r)
			break

	return pi * (r*r)

r = input('Input radius (r) : ')
print(f'{findArea(r):.3f}')
