# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 15:48:57 2020

@author: ad.1201555
"""

dict1={"name":"virat","age":30,"gender":"male"}
dict2={"name":"ptusha","age":50,"gender":"female"}

zipped=zip(dict1,dict2)

for (k1,v1) , (k2,v2) in zip(dict1.items(),dict2.items()):
        print(k1, v1)
        print(k2,v2)