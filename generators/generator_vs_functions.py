# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 08:31:24 2021

@author: Divya
"""

def arthmetic_series(a,r):
    while(a<50):
        a=a+r
        print(a)

arthmetic_series(1,8)



def arthmetic_series_generator(a,r):
    while(a<50):
        yield a
        a=a+r

s=arthmetic_series_generator(1,8)

print(s)
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
