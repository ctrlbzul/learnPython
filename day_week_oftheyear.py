# import datetime class from datetime module
from datetime import datetime

# current time
now = datetime.now()

# set day and week of the year
day_of_year = now.strftime("%-j")
week_of_year = now.strftime("%U")

# print day and week of the year
print('Today is day ' + day_of_year + ' of the year, and')
print('This week is week ' + week_of_year + ' of the year.')