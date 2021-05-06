# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:55:52 2021

@author: Divya
Figure out a data type definition 
for time records with entries for
 hours, minutes and seconds.
"""
import numpy as np

time_type=np.dtype([('h',int),('m',int),('s',int)])

time_data=np.array([(11,28,18),(12,38,9),(23,59,59)],dtype=time_type)

print(type(time_data))

print(time_data[0])

time_data[0]=(9,45,9)

print(time_data)