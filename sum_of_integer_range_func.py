# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 12:40:35 2020
@author: 666292
"""

a=[10,11,122,23,33,55,66,77,88,80,90]

sum=0
for l in a:
    print(l)
    sum=sum+l
    
print(sum)

sum=0

for l in range(len(a)):
    print(a[l])
    sum=sum+a[l]
    
print(sum)