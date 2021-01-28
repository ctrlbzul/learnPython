from menu_item import MenuItem

# set the menu
item1 = MenuItem('Sandwich', 5)
item2 = MenuItem('Chocolate Cake', 4)
item3 = MenuItem('Burger', 5)
item4 = MenuItem('Coke', 1)
item5 = MenuItem('Coffee', 3)
item6 = MenuItem('Orange Juice', 2)

# set the menu with loop
number = 0
print('// MENU //')
menus = [item1, item2, item3, item4, item5, item6]
for menu in menus:
	print(str(number) + '. ' + menu.detail())
	number += 1

while True:
	# order the menu
	print('\n// ORDER //')
	order = int(input('Enter menu item number\t: '))
	selected_item = menus[order]
	print('Selected item\t: ' + selected_item.name)

	# get the count and set the price
	item_count = int(input('Enter quantity (10% off for 3 or more): '))

	#get total price
	result = selected_item.total_price(item_count)
	print('\nYOUR ORDER\t: ' + str(item_count) + ' ' + selected_item.name)
	print('TOTAL PRICE\t: $ ' + str(result))

	again = str(input("\nWant to order again ? (y/n): "))
	if again == "n" or again == "N":
		break
print('Thanks for ordering.')


