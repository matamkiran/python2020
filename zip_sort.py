# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 15:57:10 2020

@author: ad.1201555
"""

a=[1,2,3]
b=['a','b','c']

data1=list(zip(a,b))

data1.sort()

print(data1)


data2=list(zip(b,a))

data2.sort()

print(data2)