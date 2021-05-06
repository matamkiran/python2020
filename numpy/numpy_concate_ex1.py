# -*- coding: utf-8 -*-
"""
Created on Thu May  6 19:21:06 2021

@author: Divya
"""

import numpy as np 

a= np.array([[1,2],[3,4],[5,6]])
b= np.array([[1,1],[1,1]])
c= np.concatenate((a,b))
print(c)
print(c.shape)
print(type(c))
print(c.dtype)