# list data type

# a data type that we can change
# 6 item = 6 index. index start with 0
smartphones = ["Apple", "Asus", "Realme", "Samsung", "Vivo", "Xiaomi"]

# print all data in list
print("SMARTPHONE LIST : ", smartphones)

# print some data with range
# 2:5 = print data 2-4 (5 is a boundary) 
print("LIST 2-4 : ", smartphones[2:5])

# get list length
# print(len(variableName))
print("SMARTPHONE LIST LENGTH : ", len(smartphones))

# get element length (character)
# print(len(variableName[index]))
print("SAMSUNG LENGTH : ", len(smartphones[3]))

# 4 food items
foods = ["Vegetables", "Egg", "Beef", "Sausage"]
print("FOOD LIST : ", foods)

# add an item
foods.append("Rice")
print("FOOD LIST : ", foods) # after rice added, there are 5 food items

# change an item, rice to bread
# listName[index] = newItem
foods[4] = "Potato"
print("NEW FOOD LIST : ", foods)

drinks = ["Ice Tea", "Cappucino", "Milkshake", "Cola"]
# merging list
# 1st way : mergingVariable = firstList + secondList
dailyMeals = foods + drinks
print("DAILY MEALS : ", dailyMeals) # now contain 9 items
# 2nd way : firstVariable.extend(secondVariable)
foods.extend(drinks)
print("DAILY MEALS : ", foods) # now foods list contain 9 items (0-8)

# access foods and drinks
print("BEST FOOD  : ", foods[1]) # egg
print("BEST DRINK : ", foods[5]) # ice tea

# count and sort
# foods.count("items") # counts how much item inside a list
# output is an integer (item counts)
foods.count("Egg") 
foods.count("Ice Tea")

# listName.sort() # sorting items base on the alphabet
foods.sort()
print("SORTED FOODS         : ", foods)

# reversed sorting
foods.sort(reverse=True)
print("REVERSE SORTED FOODS : ", foods)

# can contains different data type
myBio = ["Zul", 21, 171.2, True]
myBio[0] += " Ramadhan"
myBio.append("Gaming") # added to myBio list

print("MY BIO : ")
# looping list
for myItems in myBio :
    print(myItems)
