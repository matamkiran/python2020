# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 11:56:23 2021

@author: Divya
 function with  param and with return type

"""

import math


def addition(aa,bb):
    print(aa+bb)

def multiplication(m,n):
    print(m*n)

def substraction(x,y):
    print(x-y)

def division(i,j):
    print(i/j)

def square(a):
    print(a*a)

def cube(a):
    math.pow(a,3)
    

a=int(input("Enter first number:"))
b=int(input("Enter Second number:"))

while(1):
    
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. cube ")
    print("7. exit")
    n=int(input("Enter your choice to exit:"))
    if(n==7):
        break

    def switch_func(n, a,b ):
        return {
            
            '1': addition(a,b),
            '2': substraction(a,b),
            '3': multiplication(a,b),
            '4': division(a,b),
            '5': square(b),
            '6': cube(a)
            }
    switch_func(n,a,b)
    #print(x)
"""
x=addition(a,b)
y=square(a)

"""

#print(x,y)
