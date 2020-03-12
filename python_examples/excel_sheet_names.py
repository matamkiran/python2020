# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 23:08:44 2020

@author: 666292
"""

#Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file="battledeath.xlsx"

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Print sheet names
print(xls.sheet_names)

# Load a sheet into a DataFrame by name: df1

df1 = xls.parse('2004')
# Print the head of the DataFrame df1
print(df1.head())


df2 = xls.parse(0)

print(df2.head())