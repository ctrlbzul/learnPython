# Program to display the Fibonacci sequence up to n-th term
n_terms = int(input('How many terms u want?\t: '))

# first two terms (n1, n2)
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if n_terms <= 0:
  print("Please enter a positive integer!")
elif n_terms == 1:
  print("Fibonacci sequence upto {0} : {1}".format(n_terms, n1))
else:
  print('Fibonacci sequence\t: ', end = '')
  while (count < n_terms):
    print('{} '.format(n1), end='')
    n_th = n1 + n2
    # update values
    n1 = n2
    n2 = n_th
    count += 1

