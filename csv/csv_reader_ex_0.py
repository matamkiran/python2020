# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 17:45:57 2021

@author: Divya
"""

# importing csv module 
import csv 

# csv file name 
filename = "crime_sampler.csv"
data=[]
count=0

# reading csv file 
with open(filename, 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile) 
	
	# extracting each data row one by one 
	for row in csvreader:
        data.append(row)
		print(row)
