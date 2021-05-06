# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 21:17:07 2021

@author: Divya
"""

import numpy as np


x = np.array([11,22,9])
y = np.array([18,7,6])
z = np.array([1,3,5])
c = np.concatenate((x,y,z))
print(c)

a=np.concatenate((x,y),axis = 0)
print(a)

print(np.row_stack((x, y)))

print(np.column_stack((x, y)))