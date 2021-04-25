# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 08:23:25 2021

@author: Divya
"""

def callgenerator(n):
    while n<50:
        yield n**n
    
a=callgenerator(2)

print(next(a))

print(next(a))

