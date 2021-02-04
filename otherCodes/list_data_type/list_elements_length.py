# make a list
cars = ["Lamborghini", "Aston Martin", "Pagani", "Mustang", "Marcedes Benz", "Ferrari"]

# print characters length of all items in the list
i = 0 # for cars list indexes
for x in cars:
  print(x, end='')
  print(' length is', len(cars[i]), 'characters')
  # space is count as one character
  i += 1
