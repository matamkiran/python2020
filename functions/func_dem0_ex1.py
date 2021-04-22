# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:57:36 2021

@author: Divya
"""

a=int(input("Enter your first number :"))
b=int(input("Enter your second number :"))
c=int(input("Enter your third number :"))

print(a,b,c)




    
if(a>b):
    print("a is big")
else:
    print("b is big")

def biggestof3(a,b,c):
    if( (a>b) & (a>c)):
        print(a," is big")
    elif(b>c):
            print(b," is big")
    else:
        print(c,"is big")

biggestof3(a,b,c)
biggestof3(100,200,300)
