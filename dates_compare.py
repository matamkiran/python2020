"""
Import date from datetime.
Create a date object for May 9th, 2007, and assign it to the start variable.
Create a date object for December 13th, 2007, and assign it to the end variable.
Subtract start from end, to print the number of days in the resulting timedelta object.
"""

# Import date
from datetime import date

# Create a date object for May 9th, 2007
start = date(2007, 5, 9)

# Create a date object for December 13th, 2007
end = date(2007, 12, 13)

# Subtract the two dates and print the number of days
print((end - start).days)


output :

218
