# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 08:26:31 2021

@author: Divya
"""

# A Python program to demonstrate use of 
# generator object with next() 

# A generator function 
def simpleGeneratorFun(): 
	yield 1
	yield 2
	yield 3

# x is a generator object 
x = simpleGeneratorFun() 

# Iterating over the generator object using next 
print(next(x)) # In Python 3, __next__() 
print(next(x)) 
print(next(x)) 
