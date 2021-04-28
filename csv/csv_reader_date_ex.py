# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 18:10:02 2021

@author: Divya
"""

from collections import Counter 
from datetime import datetime
import csv

# Create the file object: csvfile
#csvfile = open('crime_sampler.csv', 'r')

csvfile= open('crime_sampler.csv','r')

crime_data=[]

# Create an empty list: crime_data
#crime_data = []
for row in csv.reader(csvfile):
    crime_data.append(row)
crimes_by_month=Counter()



for row in crime_data:
    date= datetime.strptime(row[0],'%m/%d/%Y %H:%M:%S')
    crimes_by_month[date.month]+=1
    

print(crimes_by_month.most_common(3))

"""
# Import necessary modules
from collection import Counter
from datetime import datetime

# Create a Counter Object: crimes_by_month
crimes_by_month = Counter()

# Loop over the crime_data list
for row in crime_data:
    
    # Convert the first element of each item into a Python Datetime Object
    date = datetime.strptime(row[0], '%m/%d/%Y %I:%M:%S %p')
    
    # Increment the counter for the month of the row by one
    crimes_by_month[date.month] += 1
    
# Print the 3 most common months for crime
print(crimes_by_month.most_common(3))
"""