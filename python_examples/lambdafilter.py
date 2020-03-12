# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:47:24 2020

@author: 666292
"""

sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = filter (lambda x: x > 4, sequences) 
print(list(filtered_result))