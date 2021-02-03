def sumListItem(item_param):
  # initial value of sum_list
  sum_list = 0
  for i in item_param:
    # adding every elements on list
    sum_list += i
  return sum_list

print('// SUM ALL THE LIST //')
print('-------------------------------')
# an empty list to store items
list_items = []

try:
  count = int(input('Item count\t: '))
  for i in range(0, count):
    item = int(input('List item\t: '))
    list_items.append(item)

except:
  print('Error : Input integer only!')

# print sum of all list items
print('\nSum of all list\t= ', end='')
print(sumListItem(list_items))
print('-------------------------------')
