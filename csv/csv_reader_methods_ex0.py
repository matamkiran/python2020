# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 17:51:57 2021

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

	print(csvreader.dialect)