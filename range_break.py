# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 13:02:04 2020

@author: 666292
"""

num=int(input("Enter a number: "))
for x in range(2,num):
    if num%x==0:
        print("{} is not prime".format(num))
        break
    else:
        print ("{} is prime".format(num))