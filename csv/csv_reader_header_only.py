# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 17:52:13 2021

@author: Divya
"""

# importing csv module 
import csv 

# csv file name 
filename = "crime_sampler.csv"

fields=[]

# reading csv file 
with open(filename, 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile) 
	
	# extracting field names through first row 
	fields = next(csvreader) 
    

print(fields)