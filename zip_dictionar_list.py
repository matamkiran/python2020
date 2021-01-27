# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:02:12 2020

@author: ad.1201555
"""

field=['name','age','gender']
values=['virat',30,'male']

data1=dict(zip(field,values))

print(data1)

field1=['bp']
values2=[99]


data1.update(zip(field1,values2))

print(data1)