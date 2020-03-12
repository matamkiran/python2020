# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 00:09:12 2020

@author: 666292
"""

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }




data={'capital':'rome','population':58.93}

europe['italy']=data
print(europe)

del europe['norway']

print(europe)