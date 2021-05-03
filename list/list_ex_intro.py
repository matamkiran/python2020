# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 08:33:46 2021

@author: Divya

List can hold mutiple value
List can have duplicate values 
List is declared in square brackets 
List maintains insertion 
List supports slicing and index based operations 
list supports negative indexing
"""

a=[10,20,30,40,50,10,20,30]
print(a)
#a=[] # empty list 
#print(a)
print(type(a))
a.append(100)
print(a)
a.append(150)
a.append(345)
print(a)
print(a[0]) 
print(a[4])

print(a[2:4])  #slicing
print(a[6:])
print(a[:6])


print(a[::-1])





