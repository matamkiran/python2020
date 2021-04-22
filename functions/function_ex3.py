# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 20:38:44 2021

@author: Divya

1.function with parameter with return type 
"""

def hello():
    print("hello am learning python")
    print("hello am learning python")
    print("hello am learning python")
    print("hello am learning python")
    print("hello am learning python")


hello()
hello()
hello()

def display(a):
    print("Your name in display is  :",a)

name=input("Enter your name :")

display(name)


def show(name):
    return "your name in show is : "+name
name=input("Enter your name :")
print(show(name))