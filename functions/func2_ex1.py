# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 11:39:33 2021

@author: Divya


1. function without param and without return type
2. function with param and without return type
3. function with param and with return type
4. function with no param and with return type

"""
def userfunc(param):
    print("Hello world ! "+ param)

def addition(a,b):
    print(a+b)  
    
userfunc(" I learningam  functions in python")

addition(1996,997)

a=[10,20,30,40,50]

def displaylist(*args):
    print(type(args))

displaylist(a,10,20,30,50,60,90,80,99,889,78)










