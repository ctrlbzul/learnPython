# taking kilometers input from user
kilometers = float(input('Enter value in kilometers\t: '))

# conversion factor
# 1 kilometer is equal to 0.621371 miles
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers, miles))

# MODIFIED ABOVE PROGRAM : MILES TO KILOMETERS
# uncomment code below to convert miles to kilometers
# # taking miles input from user
# miles = float(input('Enter value in miles\t: '))

# # conversion factor
# conv_fac = 0.621371

# # calculate kilometers
# kilometers = miles / conv_fac
# print('%0.2f miles is equal to %0.2f kilometers' %(miles, kilometers))
