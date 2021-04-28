# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 15:22:39 2021

@author: Divya
"""

# importing csv module 
import csv 

# csv file name 
filename = "crime_sampler.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 

# reading csv file 
with open(filename, 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile) 
	
	# extracting field names through first row 
	fields = next(csvreader) 

	# extracting each data row one by one 
	for row in csvreader: 
		rows.append(row) 

	# get total number of rows 
	print("Total no. of rows: %d"%(csvreader.line_num)) 

# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 

# printing first 5 rows 

print('\nFirst 5 rows are:\n') 
for row in rows[:100]: 
	# parsing each column of a row 
	for col in row: 
		print("%10s"%col), 
	print('\n') 
