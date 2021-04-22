# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 11:26:26 2021

@author: Divya
"""

def func1(n,l):
    for i in l:
        print(n ," * ", i,"=",n*i)

number=int(input("Enter the number you wish to display multiplication of table :"))
b=[1,2,3,4,5,6,7,8,9,10]


func1(number,b)

