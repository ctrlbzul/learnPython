# Python 3 program to find simple interest

'''
Simple interest formula is given by:
Simple Interest = (P x T x R)/100
Where,
P is the principle amount
T is the time and
R is the rate
'''

# function : return simple interest value
def simpleInterest(p, t, r):
  # formula
  si = (p * t * r) / 100

  return (f'''The principal is {p}\
  \nThe time period is {t}\
  \nThe rate of interest is {t}\
  \nSo, the simple interest is {si}''')

# give values and get the result
print(simpleInterest(8, 6, 8))
