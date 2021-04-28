# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 15:41:36 2021

@author: Divya
"""
#Import the csv module
import csv
# Create the file object: csvfilec
csvfile=open("crime_sampler.csv","r")
# Create an empty list: crime_data
crime_data=[]
# Loop over a csv reader on the file object
for row in csv.reader(csvfile):
    crime_data.append((row[0],row[2],row[4],row[5]))
# Remove the first element from crime_data
crime_data.pop(0)
# Print the first 10 records
print(crime_data[:2])