# Python program to display all the prime numbers within an interval

start_num = 900
end_num = 1000

print('Prime numbers between {0} and {1} are : '.format(start_num, end_num))

# looping numbers 900 - 1000
for num in range(start_num, end_num + 1):
  # all prime numbers are greater than 1
  if num > 1:
    for i in range(2, num):
      if (num %i == 0):
        break
    else:
      print(num)
