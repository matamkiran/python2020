# -*- coding: utf-8 -*-
"""
Created on Mon May 31 08:56:47 2021

@author: Divya
"""
rows=[[1,"shiva",100],
      [2,"kumar",99],
      [3,"kumar",98]]

import csv 
with open('student_data_write_list.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["sno","sutdent","marks"])
    writer.writerows(rows)
    

with open('student_data_write_list.csv','r',newline='') as file:
    csvreader=csv.reader(file)
    next(csvreader)
    for row in csvreader:
        print(row)