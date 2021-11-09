# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 07:50:06 2021

@author: matam
"""

def mylist():
    a=[10,20,30,10,20,30]
    b=10
    def nestedlist():
        #print(a)
        #print(b)
        c=100
    return nestedlist

func_call=mylist()

func_call()

print(func_call.__closure__)
print(func_call.__closure__ is None)
print(len(func_call.__closure__))