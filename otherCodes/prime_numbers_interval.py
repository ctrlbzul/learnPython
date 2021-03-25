# python program to print all  prime number in an interval
# number should be greater than 1

start_num = 11
end_num = 25

print(f'Prime numbers in {start_num} to {end_num}')
for i in range(start_num, end_num + 1):
  if i > 1:
    for j in range(2, i):
      if (i % j == 0):
        break
    else:
      print(i)
