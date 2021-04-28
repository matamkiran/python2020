# -*- coding: utf-8 -*-
"""
Created on Apr 28 15:33:27 2021

@author: Divya
"""

import csv

reader=csv.DictReader(open("crime_sampler.csv"))


for row in reader:
    if(row['Primary Type']== 'THEFT'):
        print(row)
        
