# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 21:04:52 2021

@author: Divya
"""

import numpy as np

A = np.array([ [11, 12, 13], [21, 22, 23], [31, 32, 3] ])
B = np.array([ [11, 102, 13], [201, 22, 203], [31, 32, 303] ])

print(np.dot(A,B))

print(A+B)
print(A==B)

print(np.array_equal(A,B))
print(np.array_equal(A,A))