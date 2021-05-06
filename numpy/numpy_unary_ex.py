# -*- coding: utf-8 -*-
"""
Created on Wed May  5 19:43:41 2021

@author: Divya

Unary operations in numpy array

"""

import numpy as np 
arr=np.array([[10,20,30,40],[90,80,70,20]])

print(arr.max())
#Row-wise max elements 
print(arr.max(axis=1))

#Row-wise min elements 
print(arr.min(axis=0))

print(arr.sum())

print(arr.cumsum())