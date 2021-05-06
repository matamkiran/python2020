# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 20:21:56 2021

@author: Divya
"""

import numpy as np
import pandas as pd

a=np.array([[10,20,305,50],[40,80,90,70]])

print(type(a))

print(a)

dataframe=pd.DataFrame(a,columns=['a','b','c','d'],index=range(10,12))
print("-=================")
print(dataframe)



print(dataframe.loc[10])

print(dataframe.iloc[0])