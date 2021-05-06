# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 21:21:34 2021

@author: Divya
"""
import numpy as np 

x = np.array([ 3.4])

y = np.tile(x,5) 

print(y)

x = np.array([[1, 2], [3, 4]])
print(np.tile(x, 2))

"""
x = np.array([[1, 2], [3, 4]])
print(np.tile(x, (2, 1)))

x = np.array([[1, 2], [3, 4]])
print(np.tile(x, (2, 2)))
"""