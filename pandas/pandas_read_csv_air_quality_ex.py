# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:37:13 2021

@author: matam
"""


import pandas as pd
# Load the airquality dataset
airquality = pd.read_csv('air-quality.csv', index_col='Date')

# Create a nullity DataFrame airquality_nullity
airquality_nullity = airquality.isnull()
print(airquality_nullity.head())


# Calculate total of missing values
missing_values_sum = airquality_nullity.sum()
print('Total Missing Values:\n', missing_values_sum)

# Calculate percentage of missing values
missing_values_percent = airquality_nullity.mean() * 100
print('Percentage of Missing Values:\n', missing_values_percent)