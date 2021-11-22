# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:41:06 2021

@author: matam
"""

# Import missingno as msno
import missingno as msno

import pandas as pd
# Load the airquality dataset
airquality = pd.read_csv('air-quality.csv', parse_dates=['Date'], index_col='Date')

# Create a nullity DataFrame airquality_nullity
airquality_nullity = airquality.isnull()
print(airquality_nullity.head())

# Plot amount of missingness
msno.bar(airquality)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    