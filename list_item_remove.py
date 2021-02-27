# function to print a straight line
def printLine():
  print('------------------------------')

# fruits list
fruits = ["Apple", "Banana", "Cherry", "Dragon Fruit", "Elderberry", "Finger Lime", "Grape", "Honeydew", "Indian Almond", "Jackfruit"]

# print the list
print('Fruits list items : {}'.format(len(fruits)))
printLine()
for fruit in fruits:
  print(fruit)

print('\n// Delete Item in List //')
count = int(input('Number of items to delete : '))
deleted_items = 0

# while loop to delete items
while deleted_items != count:
  item_name = input("Item name : ")
  item_name = item_name.capitalize()
  if item_name in fruits:
    fruits.remove(item_name)
    deleted_items += 1
  else:
    print('{} not found in fruits list!'.format(item_name))
  
# print list after item removal (updated list)
print('\n{} items deleted.'.format(deleted_items))
print('Fruits list items : {}'.format(len(fruits)))
printLine()
for fruit in fruits:
  print(fruit)
