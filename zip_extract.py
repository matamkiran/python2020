# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 15:54:26 2020

@author: ad.1201555
unzipping
"""

pairs=[('a',1),('b',2)]

print(type(pairs))

a,b=zip(*pairs)

print(a)
print(b)