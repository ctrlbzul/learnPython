# Python 3 program to find compound interest

'''
Formula to calculate compound interest annually is given by:
A = P(1 + R/100)^t
Compound Interest = A – P
Where,
A is amount
P is principle amount
R is the rate and
T is the time span
'''

# function : return compound interest value
def compoundInterest(principle, rate, time):
  # formula
  amount = principle * (pow((1 + rate / 100), time))
  ci = amount - principle

  return (f'Compound interest is {ci}')

# give values and get the result
print(compoundInterest(1000, 10.25, 5))
