# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:34:57 2021

@author: matam
"""

limit = int(input("Enter your limit : \n"))  #take input from enduser

numbers=[]

for i in range(limit):
    num=int(input("Enter  "+ str(i+1) +" number \n"))
    numbers.append(num)  # add numbers to list 


average = sum(numbers) / len(numbers)  # sum and len are inbuilt functions in python

print("The average of given list of values is : " + str(round(average, 2)))  # round is also inbuilt function in python 
