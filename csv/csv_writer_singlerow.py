# -*- coding: utf-8 -*-
"""
Created on Mon May 31 08:51:39 2021

@author: Divya
"""

import csv 
with open('student_data_write.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["sno","sutdent","marks"])
    writer.writerow([1,"shiva",100])
    writer.writerow([2,"kumar",99])
    writer.writerow([2,"kumar",98])
    

