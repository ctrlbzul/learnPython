# make first list
first_six_months = ["January", "February", "Third", "April", "May", "June"]
last_six_months = ["July", "August", "September", "October", "Eleventh", "December"]

# print the first and second list
print('// BEFORE CHANGING //')
print('First 6 months\t:', first_six_months)
print('Last 6 months\t:', last_six_months)

# CHANGING LIST ELEMENTS
# changes "Third" into "March" and "Eleventh" into "November"
# list_name[index] = "new name"/value
first_six_months[2] = "March"
last_six_months[4] = "November"
print('\n//AFTER BEING CHANGED //')
print('First 6 months\t:', first_six_months)
print('Last 6 months\t:', last_six_months)

# merging the list
# first way
# merging first list and second list
months_in_year = first_six_months + last_six_months
print('\nMONTHS IN YEAR(FIRST WAY)')
print('Months in a year : ', months_in_year)

# second way
# merging first list and second list with first_list.extend(second_list)
first_six_months.extend(last_six_months)
print('\nMONTHS IN YEAR(SECOND WAY)')
print('Months in a year : ', first_six_months)
