# -*- coding: utf-8 -*-
"""
Created on Wed May  5 19:54:38 2021

@author: Divya
"""
import numpy as np

datatype=[('sname','S10'),('price',float)]

values=[('dmart',1880.99),('castrol',987.89),('infosys',1530.45)]

arr=np.array(values, dtype = datatype)

print(arr)

arr.sort()
print(arr)

arr=np.sort(arr,order='price')
print(arr)