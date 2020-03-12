# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:50:47 2020

@author: 666292
"""

from functools import reduce
sequences = [1,2,3,4,5]
product = reduce (lambda x, y: x*y, sequences)
print(product)