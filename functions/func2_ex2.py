# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:22:15 2021

@author: Divya

2. function with param and with return type 

"""
def addition(*args):
    a=0
    print(args)
    for i in args:
        #print(i)
        a=a+i
    return a
   

a=addition(10,20,30,40,50,60,70,80,90)
print(a)