# add menu items and show it in a list
menu_name = str(input('Name of your menu\t: '))
count = int(input('Number of items\t\t: '))
names = [] # an empty list to store items name
prices = [] # an empty list to store items price

# adding the menu items
for i in range(0, count):
	item_name = str(input('Item name\t: '))
	names.append(item_name)
	item_price = int(input('Item price\t: '))
	prices.append(item_price)

# print menu's name
print('\n// ' + menu_name + ' //')
# print menu items name and price per line
for i, j in zip(names, prices):
	print(f"{i:>10}", end='')
	print(f"{j:>10}", end='\n')